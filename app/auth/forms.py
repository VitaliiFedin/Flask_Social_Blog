from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms.validators import ValidationError
from ..models import User
from flask_login import current_user


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                                                         'Usernames must have only '
                                                                                         'letters, numbers, dots or '
                                                                                         'underscores ')])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', 'Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered')


class PasswordUpdateForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    new_password = PasswordField('New password', validators=[DataRequired()])
    repeat_password = PasswordField('Confirm new password', validators=[DataRequired(), EqualTo('new_password',
                                                                                                'Password must match')])
    submit = SubmitField('Change')


class EmailToResetPasswordForm(FlaskForm):
    email = StringField('Enter Email to Reset Password', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password',validators=[DataRequired(), EqualTo('password2','Password must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField()


class EmailResetForm(FlaskForm):
    email = StringField('Enter new email', validators=[DataRequired(), Email()])
    confirm = SubmitField('Change email')
