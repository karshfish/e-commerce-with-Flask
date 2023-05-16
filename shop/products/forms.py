from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, DecimalField,StringField, BooleanField, TextAreaField, validators

class Addproducts(Form):
    # __tablename__ = 'Product'
    # __abstract__ = True
    name = StringField('Name', [validators.DataRequired()])
    price = DecimalField('Price', [validators.DataRequired()])
    discount = IntegerField('Discount', default=0)
    stock = IntegerField('Stock', [validators.DataRequired()])
    desc = TextAreaField('Colors', [validators.DataRequired()])
    colors = TextAreaField('Colors',[validators.DataRequired()])

    image1 = FileField("Image 1", )# validators[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'images only'])
    image2 = FileField("Image 2", )# validators[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'images only'])
    image3 = FileField("Image 3", )# validators[FileRequired(), FileAllowed(['jpg','png','gif','jpeg']), 'images only'])