from django.db import models

# Create your models here.

type_choice = (
        ("1", "Clothing"),
        ("2", "Books"),
        ("3", "Almirah"),
        ("4", "Refrigerator"),
        ("5", "Water Purifier"),
        ("6", "Gas Stove"),
        ("7", "Bed"),
        ("8", "Mattress"),
        ("9", "Chair"),
        ("10", "Fan"),
        ("11", "Item not in list"),
)

choices = (
    ("1", "Clothing"),
    ("2", "Books"),
    ("3", "Almirah"),
    ("4", "Refrigerator"),
    ("5", "Water Purifier"),
    ("6", "Gas Stove"),
    ("7", "Bed"),
    ("8", "Mattress"),
    ("9", "Chair"),
    ("10", "Fan"),
)

material = (
    ("1", "Plastic"),
    ("2", "Wood"),
)

drawers = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

mirror = (
    ("1", "Yes"),
    ("2", "No"),
)

shelves = (
    ("1", "1"),
    ("2", "2"),
)

color = (
    ("1", "Red"),
    ("2", "Blue"),
    ("3", "Green"),
    ("4", "Black"),
    ("5", "White"),
    ("6", "Yellow"),
    ("7", "Violet"),
    ("8", "Orange"),
    ("9", "Purple"),
)

door = (
    ("1", "1"),
    ("2", "2"),
)

star_rating = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

burner = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)

stove_type = (
    ("1", "Gas"),
    ("2", "Electric"),
)

bed_type = (
    ("1", "Single Bed"),
    ("2", "Double Bed"),
)

storage = (
    ("1", "YES"),
    ("2", "NO"),
)

with_mattress = (
    ("1", "YES"),
    ("2", "NO"),
)

armrest = (
    ("1", "YES"),
    ("2", "NO"),
)

foldable = (
    ("1", "YES"),
    ("2", "NO"),
)

pack_of = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)

mattress_material = (
    ("1", "Cotton"),
    ("2", "Polyester"),
    ("3", "Foam"),
)

class user_info(models.Model):
    otp_sent = False
    num_otp = models.CharField(max_length=4)
    mail_otp = models.CharField(max_length=4)
    num_verified = False
    mail_verified = False
    first_name = models.CharField(max_length = 200)
    Last_Name = models.CharField(max_length=50)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 50)
    number = models.CharField(max_length = 10)
    email = models.EmailField()
    address = models.CharField(max_length=200)

class seller_info(models.Model):
    otp_sent = False
    mail_otp = models.CharField(max_length=4)
    num_otp = models.CharField(max_length=4)
    num_verified = False
    mail_verified = False
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 50)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    enterprise_name = models.CharField(max_length=200)

class add_product(models.Model):
    #BASIC INFO
    product_brand = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100, choices=type_choice)
    product_name = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    mobile_no = models.CharField(max_length=10)
    product_img = models.ImageField(upload_to='images/')

    product_img1 = models.ImageField(upload_to='images/', null = True, blank = True)
    product_img2 = models.ImageField(upload_to='images/', null = True, blank = True)
    product_img3 = models.ImageField(upload_to='images/', null = True, blank = True)
    product_img4 = models.ImageField(upload_to='images/', null = True, blank = True)

    # ALMIRAH
    material = models.CharField(max_length=100, choices=material, blank=True, null = True)
    drawers = models.CharField(max_length=100, choices=drawers, blank=True, null = True)
    color = models.CharField(max_length=100, choices=color, blank=True, null = True)
    length = models.PositiveIntegerField(blank=True, null = True)
    breadth = models.PositiveIntegerField(blank=True, null = True)
    height = models.PositiveIntegerField(blank=True, null = True)
    launch_year = models.DateField(blank=True, null = True)
    weight = models.PositiveIntegerField(blank=True, null = True)
    rent = models.PositiveIntegerField(blank=True, null = True)
    duration = models.CharField(max_length=100, null = True)
    # FRIDGE
    door = models.CharField(max_length=100, choices=door, blank=True, null = True)
    rating = models.CharField(max_length=100, choices=star_rating, blank=True, null = True)
    capacity = models.PositiveIntegerField(blank=True, null = True)
    # STOVE
    burner = models.CharField(max_length=100, choices=burner, blank=True, null = True)
    stove_type = models.CharField(max_length=100, choices=stove_type, blank=True, null = True)
    # BED
    mattress_material = models.CharField(max_length=100, choices=mattress_material, blank=True, null = True)
    bed_type = models.CharField(max_length=100, choices=bed_type, blank=True, null = True)
    storage = models.CharField(max_length=100, choices=storage, blank=True, null = True)
    with_mattress = models.CharField(max_length=100, choices=with_mattress, blank=True, null = True)
    # chair
    armrest = models.CharField(max_length=100, choices=armrest, blank=True, null = True)
    foldable = models.CharField(max_length=100, choices=foldable, blank=True, null = True)
    pack_of = models.CharField(max_length=100, choices=pack_of, blank=True, null = True)