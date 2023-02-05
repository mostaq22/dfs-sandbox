from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, TextAreaField, IntegerField, SelectField
from wtforms.validators import InputRequired, Length, optional


class Login(FlaskForm):
    username = StringField('username', validators=[
                           InputRequired(), Length(min=5, max=15)])
    password = PasswordField('password', validators=[
                             InputRequired(), Length(min=5, max=15)])
    remember = BooleanField('rememer me')


class Registry(FlaskForm):
    endpoint = StringField('username', validators=[
                           InputRequired(), Length(min=1, max=100)])
    payload = TextAreaField('Payload', validators=[InputRequired()])
    response = TextAreaField('Response', validators=[InputRequired()])
    description = TextAreaField('description', validators=[optional(),])


RegistryData = [
    {"id": 1, "name": "test 1"},
    {"id": 2, "name": "test 2"},
    {"id": 3, "name": "test 3"}
]


class Transaction(FlaskForm):
    register = SelectField('Registry',  validators=[InputRequired()], choices=[
                           ('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    payload = TextAreaField('Payload', validators=[InputRequired()])
    response = TextAreaField('Response', validators=[InputRequired()])
    description = TextAreaField('description', validators=[optional(), ])

    def __init__(self):
        super(Transaction, self).__init__()
        # self.category.choices = [(c.id, c.name) for c in Category.query.all()]
        # category = QuerySelectField(query_factory=lambda: Category.query.all())
        self.register.choices = [(c.get('id'), c.get('name'))
                                 for c in RegistryData]
