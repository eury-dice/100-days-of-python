from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

coffee_choices = ['✘']
c_choice = ''
wifi_choices = ['✘']
w_choice = ''
power_choices = ['✘']
p_choice = ''

for _ in range(1, 6):
    c_choice += '☕'
    w_choice += '📶'
    p_choice += '🔌'

    coffee_choices.append(c_choice)
    wifi_choices.append(w_choice)
    power_choices.append(p_choice)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location on Google Maps (URL)', validators=[DataRequired(), URL()])
    open_time = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee = SelectField('Coffee Rating', choices=coffee_choices, validators=[DataRequired()])
    wifi = SelectField('Wi-Fi Strength Rating', choices=wifi_choices, validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices=power_choices, validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=["POST", "GET"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        with open('cafe-data.csv', mode='a', encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open_time.data},"
                           f"{form.close_time.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")

        return redirect('/cafes')
    else:
        return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf=8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
