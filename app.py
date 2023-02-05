from dataclasses import dataclass
from flask import Flask, render_template, redirect, jsonify
from forms import Login as LoginForm, Registry as RegistryForm, Transaction as TransactionForm
from flask_sqlalchemy import SQLAlchemy
from flask import request

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config["SECRET_KEY"] = "s78d6#fas87#d6f8as7df6a@s8d7f6as8d"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///home/mostaq/Documents/dfstech/dfs-sandbox/sandbox.db'

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

@dataclass
class Registry(db.Model):
    id: int
    endpoint: str
    payload: str
    response: str

    id = db.Column(db.Integer, primary_key=True)
    endpoint = db.Column(db.String(80), unique=True, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Registry %r>' % self.endpoint


class ApiTransaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    registry = db.Column(db.Integer, unique=True, nullable=False)
    payload = db.Column(db.Text, nullable=False)
    response = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)

    # category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
    #     nullable=False)
    # category = db.relationship('Category',
    #     backref=db.backref('posts', lazy=True))

    def __repr__(self):
        return '<Transaction %s>' % self.registry

@app.route('/', methods=['GET'])
def home():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/login', methods=['POST'])
def login_submit():
    form = LoginForm()
    if form.validate_on_submit():
        return form.username.data + "--"+ form.password.data
    return render_template('login.html', form=form)

@app.route('/dashboard')
def dasboard():
    return render_template('dashboard.html')

@app.route('/api-registry')
def api_registry_list():
    registry = Registry.query.all()
    return render_template('registry/list.html', registry=registry)

@app.route('/create-api-registry', methods=['GET','POST'])
def api_registry_create():
    form = RegistryForm()
    if form.validate_on_submit():
        new_registry = Registry(endpoint=form.endpoint.data, payload=form.payload.data, response=form.response.data, description=form.description.data)
        db.session.add(new_registry)
        db.session.commit()

        if request.form.get('save_add_more'):
            return redirect('/create-api-registry')
    return render_template('registry/create.html', form=form)

@app.route('/transactions')
def transaction():
    transactions = ApiTransaction.query.all()
    return render_template('transactions/list.html', transactions=transactions)

@app.route('/create-transactions', methods=['GET','POST'])
def transaction_create():
    form = TransactionForm()
    if form.validate_on_submit():
        data = {
            "registry": form.register.data,
            "payload": form.payload.data,
            "response": form.response.data,
            "description": form.description.data,
            "user_id": 1 # hardcoded
        }
        transaction = ApiTransaction(**data)
        db.session.add(transaction)
        db.session.commit()

        if request.form.get('save_add_more'):
            return redirect('/create-transactions')
    return render_template('transactions/create.html', form=form)



@app.route('/registry/<id>')
def get_registry_detail(id: int):
    return jsonify(Registry.query.filter_by(id=id).first())