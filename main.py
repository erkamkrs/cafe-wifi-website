from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class CafeForm(FlaskForm):
    cafe_name = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time ex. 8 AM', validators=[DataRequired()])
    closing_time = StringField('Closing Time ex. 9 PM', validators=[DataRequired()])
    coffee_rating = SelectField("Coffee Rating", choices=["💩", "🤢", "😬", "😋", "🤤"], validators=[DataRequired()])
    wifi_rating = SelectField("Wifi Rating", choices=["🐌", "👎", "😬", "👌", "⚡️"], validators=[DataRequired()])
    service_rating = SelectField("Service Rating", choices=["💩", "👎", "😬", "👌", "🌟️"], validators=[DataRequired()])
    location_rating = SelectField("Location Rating", choices=["💩", "👎", "😬", "👌", "🌟️"], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cafes_list")
def cafes_():
    with open("cafes.csv", newline="") as file:
        data = csv.reader(file, delimiter=',')
        rows_list = []
        for row in data:
            rows_list.append(row)
    return render_template("cafes.html", cafes_list=rows_list)

@app.route("/add")
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafes.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.service_rating.data}"
                           f"{form.location.data},")
        return redirect(url_for('cafes_'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
