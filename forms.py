from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField, RadioField, SelectField
from wtforms.validators import DataRequired, URL

# WTForm


class AddCafeForm(FlaskForm):
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    google_maps_url = StringField("Google Maps URL", validators=[DataRequired()])
    img_url = StringField("Cafe Image URL", validators=[DataRequired(), URL()])
    cafe_location = StringField("Cafe Location", validators=[DataRequired()])
    socket_availability = SelectField('Any Sockets There?', coerce=bool, choices=[(True, 'Yes'), (False, "No")])
    toilet_availability = SelectField('Are There Toilets?', coerce=bool, choices=[(True, 'Yes'), (False, "No")])
    wifi_availability = SelectField('Is There WiFi?', coerce=bool, choices=[(True, 'Yes'), (False, "No")])
    phone_call_availability = SelectField('Can You Take Phone calls?', coerce=bool, choices=[(True, 'Yes'), (False, "No")])
    seat_count = SelectField("Total Numbers Of Seats:",
                             choices=['0-10', '10-20', '20-30', '30-40', '50+'])
    coffee_price = FloatField("How Much Is A Black Coffee?")
    submit = SubmitField("Submit New Cafe")
