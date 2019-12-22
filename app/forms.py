from flask_wtf import   FlaskForm
from wtforms import BooleanField,StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password',validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
