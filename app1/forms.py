from django import forms
from app1.models import *
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import re


# FUNCTION TO VALIDATE IMAGE SIZE
def file_size(value):
    limit = 5242880
    if value.size > limit:
        raise ValidationError(_("File size should be less than 5mb"))


class Login(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=50)

    def clean_password(self):
        data = self.cleaned_data['password']

        num_int = 0
        num_char = 0

        for char in data:
            if char.isdigit():
                num_int += 1
            num_char += 1

        if num_int < 2:
            if num_char < 8:
                raise ValidationError(_("Invalid password"))

        return data


class user_Details(forms.Form):
    First_Name = forms.CharField(max_length=200)
    Last_Name = forms.CharField(max_length=50)
    Address = forms.CharField(max_length=200)


class Signup(forms.Form):
    email = forms.EmailField()
    paswrd = forms.CharField(max_length=50)
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=50)

    def clean_password(self):
        data = self.cleaned_data['password']

        num_int = 0
        num_char = 0

        for char in data:
            if char.isdigit():
                num_int += 1
            num_char += 1

        if num_int < 2:
            if num_char < 8:
                raise ValidationError(_("Invalid password"))

        return data


class seller_Details(forms.Form):
    First_Name = forms.CharField(max_length=200)
    Last_Name = forms.CharField(max_length=50)
    Enterprise_Address = forms.CharField(max_length=200)
    Enterprise_Name = forms.CharField(max_length=200)

    def clean_Telephone_No(self):
        data = self.cleaned_data["Telephone_No"]

        pattern = "^[6-9]\d{9}$"
        match = re.search(pattern, data)

        if not match:
            raise ValidationError(_("Invalid number"))

        return data


class Add_Product(forms.Form):
    product_name = forms.CharField(max_length=100)
    product_img = forms.ImageField(validators=[file_size])
    product_brand = forms.CharField()
    product_type = forms.ChoiceField(choices=type_choice)
    description = forms.CharField(max_length=10000, widget=forms.Textarea)

class Almirah_Specs(forms.Form):
    material = forms.ChoiceField(choices=material)
    drawers = forms.ChoiceField(choices=drawers)
    color = forms.ChoiceField(choices=color)
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    height = forms.IntegerField()
    launch_year = forms.DateField(widget=forms.SelectDateWidget)
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])

class Almirah_Filter(forms.Form):
    material = forms.ChoiceField(choices=material)
    drawers = forms.ChoiceField(choices=drawers)
    color = forms.ChoiceField(choices=color)
    rent = forms.IntegerField()

class Fridge_Specs(forms.Form):
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    height = forms.IntegerField()
    launch_year = forms.DateField(widget=forms.SelectDateWidget)
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)
    door = forms.ChoiceField(choices=door)
    rating = forms.ChoiceField(choices=star_rating)
    capacity = forms.IntegerField()
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])

class Fridge_Filter(forms.Form):
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)
    door = forms.ChoiceField(choices=door)
    rating = forms.ChoiceField(choices=star_rating)
    capacity = forms.IntegerField()

class Stove_Specs(forms.Form):
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    height = forms.IntegerField()
    launch_year = forms.DateField(widget=forms.SelectDateWidget)
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)
    burner = forms.ChoiceField(choices=burner)
    stove_type = forms.ChoiceField(choices=stove_type)
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])

class Stove_Filter(forms.Form):
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)
    burner = forms.ChoiceField(choices=burner)
    stove_type = forms.ChoiceField(choices=stove_type)

class Bed_Specs(forms.Form):
    color = forms.ChoiceField(choices=color)
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    height = forms.IntegerField()
    launch_year = forms.DateField(widget=forms.SelectDateWidget)
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])
    bed_type = forms.ChoiceField(choices=bed_type)
    storage = forms.ChoiceField(choices=storage)
    with_mattress = forms.ChoiceField(choices=with_mattress)

class Bed_Filter(forms.Form):
    color = forms.ChoiceField(choices=color)
    rent = forms.IntegerField()
    bed_type = forms.ChoiceField(choices=bed_type)
    storage = forms.ChoiceField(choices=storage)
    with_mattress = forms.ChoiceField(choices=with_mattress)

class Mattress_Specs(forms.Form):
    material = forms.ChoiceField(choices=material)
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    height = forms.IntegerField()
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])
    bed_type = forms.ChoiceField(choices=bed_type)

class Mattress_Filter(forms.Form):
    material = forms.ChoiceField(choices=material)
    rent = forms.IntegerField()
    bed_type = forms.ChoiceField(choices=bed_type)

class Chair_Specs(forms.Form):
    material = forms.ChoiceField(choices=material)
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    height = forms.IntegerField()
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])
    armrest = forms.ChoiceField(choices=armrest)
    foldable = forms.ChoiceField(choices=foldable)
    pack_of = forms.ChoiceField(choices=pack_of)

class Chair_Filter(forms.Form):
    material = forms.ChoiceField(choices=material)
    rent = forms.IntegerField()
    armrest = forms.ChoiceField(choices=armrest)
    foldable = forms.ChoiceField(choices=foldable)
    pack_of = forms.ChoiceField(choices=pack_of)

class Fan_Specs(forms.Form):
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    launch_year = forms.DateField(widget=forms.SelectDateWidget)
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])

class Fan_Filter(forms.Form):
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)

class Purifier_Specs(forms.Form):
    length = forms.IntegerField()
    breadth = forms.IntegerField()
    height = forms.IntegerField()
    launch_year = forms.DateField(widget=forms.SelectDateWidget)
    weight = forms.IntegerField()
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)
    rating = forms.ChoiceField(choices=star_rating)
    capacity = forms.IntegerField()
    product_img1 = forms.ImageField(validators=[file_size])
    product_img2 = forms.ImageField(validators=[file_size])
    product_img3 = forms.ImageField(validators=[file_size])
    product_img4 = forms.ImageField(validators=[file_size])

class Purifier_Filter(forms.Form):
    rent = forms.IntegerField()
    color = forms.ChoiceField(choices=color)
    rating = forms.ChoiceField(choices=star_rating)
    capacity = forms.IntegerField()

class Verify_Mobile(forms.Form):
    number = forms.CharField(max_length=10, min_length=10)

    def clean_number(self):
        data = self.cleaned_data["number"]

        pattern = "^[6-9]\d{9}$"
        match = re.search(pattern, data)

        if not match:
            raise ValidationError(_("Invalid number"))

        return data

class Verify_Email(forms.Form):
    otp = forms.CharField(max_length=4, min_length=4)
    
class Choice(forms.Form):
    product_type = forms.ChoiceField(choices=choices)