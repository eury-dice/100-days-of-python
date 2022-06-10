from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class RatingForm(FlaskForm):
    rating = StringField(label="Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = TextAreaField(label="Your Review", validators=[DataRequired()], render_kw={'class': 'form-control', 'rows': 5})
    submit = SubmitField(label="Done")


class MovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")
