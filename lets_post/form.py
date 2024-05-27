from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from lets_post.models import User

class RegistrationForm(FlaskForm):
    '''
        A class for the registrationform
    '''
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4, max =100)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit= SubmitField('Sign Up')
   
    def validate_username(self, username):
        '''
        creating a custom validation for my registrationform which will prevent users
        not to use already used username ---document from wtf form documentations 
        '''
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken Please choose another username')
    
    def validate_email(self, email):
        '''
        creating a custom validation for my registrationform which will prevent users
        not to use already used email ---document from wtf form documentations 
        '''
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken Please choose another username')
    
    
class LoginForm(FlaskForm):
    '''A class of the login form'''
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password',validators=[DataRequired(),Length(min=4, max =100)])
    remember = BooleanField('Remember Me')
    submit= SubmitField('Login')
    

class UpdateAccountForm(FlaskForm):
    '''
        A class for updating user account 
    '''
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[Email(), DataRequired()])
    submit= SubmitField('Update')
   
    def validate_username(self, username):
        '''
        creating a custom validation for my updateaccountform which will prevent users
        not to use already used username ---document from wtf form documentations 
        '''
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken Please choose another username')
    
    def validate_email(self, email):
        '''
        creating a custom validation for my registrationform which will prevent users
        not to use already used email ---document from wtf form documentations 
        '''
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken Please choose another username')
    
    
    