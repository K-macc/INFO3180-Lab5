from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileField, FileAllowed

# Add any form classes for Flask-WTF here
class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[InputRequired()])
    description = TextAreaField('Decription', validators=[InputRequired()])
    poster = FileField('Posters', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only! (JPG, PNG)'])])
    