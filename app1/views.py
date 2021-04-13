from django.shortcuts import render
from app1.models import*
from app1.forms import*
from django.shortcuts import redirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
import random

# Create your views here.

def user_login(request):
    if request.method == "POST":
        form = Login(request.POST)

        if form.is_valid():
            if user_info.objects.filter(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password']).exists():
                user = user_info.objects.filter(username=form.cleaned_data['username'],
                                                password=form.cleaned_data['password'])

                if user.mail_verified == True:
                    user = user_info.objects.get(username=form.cleaned_data['username'],
                                                 password=form.cleaned_data['password'])
                    request.session["email"] = user.email

                    return redirect(reverse("user_home"))
                    # return render(request, 'my_site/home_page.html', context=context)

    else:
        form = Login()

    context = {
        'form': form,
    }

    return render(request, 'app1/user_login_page.html', context=context)


def user_details(request):
    if request.method == "POST":
        form = user_Details(request.POST)

        if form.is_valid():
            user = user_info.objects.get(username=request.session["username"],
                                         password=request.session["password"])

            user.email = request.session['email']
            user.first_name = form.cleaned_data['First_Name']
            user.last_name = form.cleaned_data['Last_Name']
            user.address = form.cleaned_data['Address']

            '''
            context = {
                "username": request.session['username'],
                "password": request.session['password'],
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "number": user.number,
                "address": user.address,
            }
            '''
            user.save()

            del request.session['username']
            del request.session['password']

            return redirect(reverse("user_home"))
            # return render(request, "my_site/home_page.html")

    else:
        form = user_Details()

    context = {
        'form': form,
    }
    return render(request, "app1/user_details_page.html", context=context)


def user_signup(request):
    if request.method == "POST":
        form = Signup(request.POST)

        if form.is_valid():

            if form.cleaned_data['password'] == form.cleaned_data['paswrd']:
                user = user_info()
                user.password = form.cleaned_data['password']
                user.username = form.cleaned_data['username']
                user.save()

                request.session['email'] = form.cleaned_data['email']
                request.session['username'] = form.cleaned_data['username']
                request.session['password'] = form.cleaned_data['password']

                return redirect(reverse('verify_email'))

            else:
                pass

    else:
        form = Signup()

    context = {
        "form": form
    }

    return render(request, "app1/user_signup_page.html", context)


def seller_login(request):
    if request.method == "POST":
        form = Login(request.POST)

        if form.is_valid():
            if seller_info.objects.filter(username=form.cleaned_data['username'],
                                          password=form.cleaned_data['password']).exists():
                user = seller_info.objects.get(username=form.cleaned_data['username'],
                                               password=form.cleaned_data['password'])
                if user.mail_verified == True:
                    request.session['email'] = user.email

                    return render(request, "app1/seller_home_page.html")

    else:
        form = Login()

    context = {
        'form': form,
    }

    return render(request, 'app1/seller_login_page.html', context=context)


def seller_signup(request):
    if request.method == "POST":
        form = Signup(request.POST)

        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['paswrd']:
                user = seller_info()

                user.password = form.cleaned_data['password']
                user.username = form.cleaned_data['username']
                user.save()

                request.session['email'] = form.cleaned_data['email']
                request.session['username'] = form.cleaned_data['username']
                request.session['password'] = form.cleaned_data['password']

                return redirect(reverse('Verify_Email'))

            else:
                pass
    else:
        form = Signup()

    context = {
        "form": form
    }

    return render(request, "app1/seller_signup_page.html", context)


def seller_details(request):
    if request.method == "POST":
        form = seller_Details(request.POST)

        if form.is_valid():
            user = seller_info.objects.get(username=request.session["username"],
                                           password=request.session["password"])

            user.first_name = form.cleaned_data['First_Name']
            user.last_name = form.cleaned_data['Last_Name']
            user.address = form.cleaned_data['Enterprise_Address']
            user.enterprise_name = form.cleaned_data['Enterprise_Name']

            '''
            context = {
                "username": request.session['username'],
                "password": request.session['password'],
                "first_name": form.cleaned_data['First_Name'],
                "last_name": form.cleaned_data['Last_Name'],
                "email": form.cleaned_data['Email'],
                "number": form.cleaned_data['Telephone_No'],
                "address": form.cleaned_data['Enterprise_Address'],
                "shop_name": form.cleaned_data['Enterprise_Name'],
            }
            '''
            user.save()

            del request.session['username']
            del request.session['password']

            return render(request, "app1/seller_home_page.html")

    else:
        form = seller_Details()

    context = {
        'form': form,
    }
    return render(request, "app1/seller_details_page.html", context=context)

def almirah(request):
    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

    context = {
        "obj_lst": obj_lst,
    }

    return render(request, "app1/products_page.html", context)

def refrigerator(request):
    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

    context = {
        "obj_lst": obj_lst,
    }
    

    return render(request, "app1/products_page.html", context)

def


def user_home(request):
    if request.method == "POST":
        form = Choice(request.POST)

        if form.is_valid():
            request.session['product_type'] = form.cleaned_data['product_type']

            if request.session['product_type'] == "1":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    return redirect(reverse("almirah"))

                else:
                    pass

            elif request.session['product_type'] == "2":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("almirah"))

                else:
                    pass

            elif request.session["product_type"] == "3":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("almirah"))

                else:
                    pass

            elif request.session["product_type"] == "4":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("refrigerator"))

                else:
                    pass

            elif request.session["product_type"] == "5":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("purifier"))

                else:
                    pass

            elif request.session["product_type"] == "6":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("stove"))

                else:
                    pass

            elif request.session["product_type"] == "7":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("bed"))

                else:
                    pass

            elif request.session["product_type"] == "8":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("mattress"))

                else:
                    pass

            elif request.session["product_type"] == "9":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("chair"))

                else:
                    pass

            elif request.session["product_type"] == "10":
                if add_product.objects.filter(product_type=form.cleaned_data['product_type']).exists():
                    obj_lst = add_product.objects.filter(product_type=form.cleaned_data['product_type'])

                    context = {
                        "obj_lst": obj_lst,
                    }

                    return redirect(reverse("fan"))

                else:
                    pass

    else:
        form = Choice()

    context = {
        "form": form,
    }

    return render(request, "app1/home_page.html", context)

def contact(request):
    return render(request, "app1/contact_page.html")

def add_products(request):
    if request.method == "POST":
        form = Add_Product(request.POST, request.FILES)

        if form.is_valid():
            request.session['product_name'] = form.cleaned_data['product_name']
            request.session['product_type'] = form.cleaned_data['product_type']
            
            product = add_product()

            product.mobile_no = request.session['tele']
            product_product_img = form.cleaned_data['product_img']
            product.product_name = form.cleaned_data['product_name']
            product.product_type = form.cleaned_data['product_type']
            product.product_brand = form.cleaned_data['product_brand']
            product.description = form.cleaned_data['description']

            product.save()

            return redirect(reverse("add_specs"))

    else:
        form = Add_Product()

    context = {
        "form": form,
    }

    return render(request, "app1/add_product_page.html", context)

def my_products(request):
    i = 1
    context = {}

    if add_product.objects.filter(mobile_no=request.session['tele']).exists():
        for item in add_product.objects.filter(mobile_no=request.session['tele']):
            context[i] = item
            i += 1

        return render(request, "app1/my_products_page.html", context=context)
    else:
        return render(request, "app1/empty_product_page.html")


def user_profile(request):
    user = user_info.objects.filter(email=request.session['email'])

    if request.method == "POST":
        form = user_Details(request.POST)

        if user.first_name != form.cleaned_data['First_Name']:
            user.first_name != form.cleaned_data['First_Name']
        if user.last_name != form.cleaned_data['Last_Name']:
            user.last_name != form.cleaned_data['Last_Name']
        if user.address != form.cleaned_data['Address']:
            user.address != form.cleaned_data['Address']

        user.save()

        return render(request, "app1/home_page.html")

    else:
        form = user_Details()

    context = {
        "form": form,
    }

    return render(request, "app1/user_update_page.html", context=context)


def seller_profile(request):
    user = seller_info.objects.filter(number=request.session['tele'])

    if request.method == "POST":
        form = seller_Details(request.POST)

        if user.first_name != form.cleaned_data['First_Name']:
            user.first_name != form.cleaned_data['First_Name']
        if user.last_name != form.cleaned_data['Last_Name']:
            user.last_name != form.cleaned_data['Last_Name']
        if user.address != form.cleaned_data['Enterprise_Address']:
            user.address != form.cleaned_data['Enterprise_Address']
        if user.enterprise_name != form.cleaned_data['Enterprise_Name']:
            user.enterprise_name != form.cleaned_data['Enterprise_Name']

        user.save()

        return render(request, "app1/seller_home_page.html")

    else:
        form = seller_Details()

    context = {
        "form": form,
    }

    return render(request, "app1/seller_update_page.html", context=context)

def add_specs1(request):
    pass

'''
def add_specs2(request):
    pass

def add_specs3(request):
    

def add_specs4(request):
    

def add_specs5(request):
   

def add_specs6(request):
    

def add_specs7(request):
    del request.session['product_type']

   

def add_specs8(request):
    del request.session['product_type']

    

def add_specs9(request):
    del request.session['product_type']
'''

def add_specs(request):
    if request.method == "POST":
        if request.session['product_type'] == "1":
            pass

        elif request.session['product_type'] == "2":
            pass

        elif request.session['product_type'] == "3":
            form = Almirah_Specs(request.POST, request.FILES)

            if form.is_valid():
                product = add_product.objects.get(mobile_no=request.session["tele"],
                                                      product_name=request.session["product_name"])

                product.material = form.cleaned_data["material"]
                product.drawers = form.cleaned_data["drawers"]
                product.color = form.cleaned_data["color"]
                product.length = form.cleaned_data["length"]
                product.breadth = form.cleaned_data["breadth"]
                product.height = form.cleaned_data["height"]
                product.launch_year = form.cleaned_data["launch_year"]
                product.weight = form.cleaned_data["weight"]
                product.rent = form.cleaned_data["rent"]
                product.product_img1 = form.cleaned_data["product_img1"]
                product.product_img2 = form.cleaned_data["product_img2"]
                product.product_img3 = form.cleaned_data["product_img3"]
                product.product_img4 = form.cleaned_data["product_img4"]
                product.duration = "month"

                product.save()

                return render(request, "app1/seller_home_page.html")

        elif request.session["product_type"] == "4":
            form = Fridge_Specs(request.POST, request.FILES)

            product = add_product.objects.filter(mobile_no=request.session["tele"],
                                                 product_name=request.session["product_name"])

            product.material = form.cleaned_data["material"]
            product.door = form.cleaned_data['door']
            product.rating = form.cleaned_data["rating"]
            product.capacity = form.cleaned_data["capacity"]
            product.color = form.cleaned_data["color"]
            product.length = form.cleaned_data["length"]
            product.breadth = form.cleaned_data["breadth"]
            product.height = form.cleaned_data["height"]
            product.launch_year = form.cleaned_data["launch_year"]
            product.weight = form.cleaned_data["weight"]
            product.rent = form.cleaned_data["rent"]
            product.duration = "month"
            product.product_img1 = form.cleaned_data["product_img1"]
            product.product_img2 = form.cleaned_data["product_img2"]
            product.product_img3 = form.cleaned_data["product_img3"]
            product.product_img4 = form.cleaned_data["product_img4"]

            product.save()

            return render(request, "app1/seller_home_page.html")

        elif request.session["product_type"] == "5":
            form = Purifier_Specs(request.POST, request.FILES)

            product = add_product.objects.filter(mobile_no=request.session["tele"],
                                                 product_name=request.session["product_name"])

            product.material = form.cleaned_data["material"]
            product.rating = form.cleaned_data["rating"]
            product.capacity = form.cleaned_data["capacity"]
            product.color = form.cleaned_data["color"]
            product.length = form.cleaned_data["length"]
            product.breadth = form.cleaned_data["breadth"]
            product.height = form.cleaned_data["height"]
            product.launch_year = form.cleaned_data["launch_year"]
            product.weight = form.cleaned_data["weight"]
            product.rent = form.cleaned_data["rent"]
            product.duration = "month"
            product.product_img1 = form.cleaned_data["product_img1"]
            product.product_img2 = form.cleaned_data["product_img2"]
            product.product_img3 = form.cleaned_data["product_img3"]
            product.product_img4 = form.cleaned_data["product_img4"]

            product.save()

            return render(request, "app1/seller_home_page.html")

        elif request.session["product_type"] == "6":
            form = Stove_Specs(request.POST, request.FILES)

            product = add_product.objects.filter(mobile_no=request.session["tele"],
                                                 product_name=request.session["product_name"])

            product.material = form.cleaned_data["material"]
            product.color = form.cleaned_data["color"]
            product.length = form.cleaned_data["length"]
            product.breadth = form.cleaned_data["breadth"]
            product.height = form.cleaned_data["height"]
            product.launch_year = form.cleaned_data["launch_year"]
            product.weight = form.cleaned_data["weight"]
            product.rent = form.cleaned_data["rent"]
            product.product_img1 = form.cleaned_data["product_img1"]
            product.product_img2 = form.cleaned_data["product_img2"]
            product.product_img3 = form.cleaned_data["product_img3"]
            product.product_img4 = form.cleaned_data["product_img4"]
            product.duration = "month"
            product.burner = form.cleaned_data["burner"]
            product.stove_type = form.cleaned_data["stove_type"]

            product.save()

            return render(request, "app1/seller_home_page.html")

        elif request.session["product_type"] == "7":
            form = Bed_Specs(request.POST, request.FILES)

            product = add_product.objects.filter(mobile_no=request.session["tele"],
                                                 product_name=request.session["product_name"])

            product.bed_type = form.cleaned_data["bed_type"]
            product.storage = form.cleaned_data["storage"]
            product.with_mattress = form.cleaned_data["with_mattress"]
            product.color = form.cleaned_data["color"]
            product.length = form.cleaned_data["length"]
            product.breadth = form.cleaned_data["breadth"]
            product.height = form.cleaned_data["height"]
            product.launch_year = form.cleaned_data["launch_year"]
            product.weight = form.cleaned_data["weight"]
            product.rent = form.cleaned_data["rent"]
            product.duration = "month"
            product.product_img1 = form.cleaned_data["product_img1"]
            product.product_img2 = form.cleaned_data["product_img2"]
            product.product_img3 = form.cleaned_data["product_img3"]
            product.product_img4 = form.cleaned_data["product_img4"]

            product.save()

            return render(request, "app1/seller_home_page.html")

        elif request.session["product_type"] == "8":
            form = Mattress_Specs(request.POST, request.FILES)

            product = add_product.objects.filter(mobile_no=request.session["tele"],
                                                 product_name=request.session["product_name"])

            product.bed_type = form.cleaned_data["bed_type"]
            product.material = form.cleaned_data["material"]
            product.length = form.cleaned_data["length"]
            product.breadth = form.cleaned_data["breadth"]
            product.height = form.cleaned_data["height"]
            product.launch_year = form.cleaned_data["launch_year"]
            product.weight = form.cleaned_data["weight"]
            product.rent = form.cleaned_data["rent"]
            product.duration = "month"
            product.product_img1 = form.cleaned_data["product_img1"]
            product.product_img2 = form.cleaned_data["product_img2"]
            product.product_img3 = form.cleaned_data["product_img3"]
            product.product_img4 = form.cleaned_data["product_img4"]

            product.save()

            return render(request, "app1/seller_home_page.html")

        elif request.session["product_type"] == "9":
            form = Chair_Specs(request.POST, request.FILES)

            product = add_product.objects.filter(mobile_no=request.session["tele"],
                                                 product_name=request.session["product_name"])

            product.armrest = form.cleaned_data["armrest"]
            product.foldable = form.cleaned_data["foldable"]
            product.pack_of = form.cleaned_data["pack_of"]
            product.material = form.cleaned_data["material"]
            product.length = form.cleaned_data["length"]
            product.breadth = form.cleaned_data["breadth"]
            product.height = form.cleaned_data["height"]
            product.weight = form.cleaned_data["weight"]
            product.rent = form.cleaned_data["rent"]
            product.duration = "month"
            product.product_img1 = form.cleaned_data["product_img1"]
            product.product_img2 = form.cleaned_data["product_img2"]
            product.product_img3 = form.cleaned_data["product_img3"]
            product.product_img4 = form.cleaned_data["product_img4"]

            product.save()

            return render(request, "app1/seller_home_page.html")

        elif request.session["product_type"] == "10":
            form = Fan_Specs(request.POST, request.FILES)

            product = add_product.objects.filter(mobile_no=request.session["tele"],
                                                 product_name=request.session["product_name"])

            product.material = form.cleaned_data["material"]
            product.color = form.cleaned_data["color"]
            product.length = form.cleaned_data["length"]
            product.breadth = form.cleaned_data["breadth"]
            product.launch_year = form.cleaned_data["launch_year"]
            product.weight = form.cleaned_data["weight"]
            product.rent = form.cleaned_data["rent"]
            product.duration = "month"
            product.product_img1 = form.cleaned_data["product_img1"]
            product.product_img2 = form.cleaned_data["product_img2"]
            product.product_img3 = form.cleaned_data["product_img3"]
            product.product_img4 = form.cleaned_data["product_img4"]

            product.save()

            return render(request, "app1/seller_home_page.html", context)

    else:
        if request.session['product_type'] == "10":
            form = Fan_Specs()

            context = {
                "form": form,
            }

            return render(request, "app1/fan_specs.html", context)

        elif request.session['product_type'] == "9":
            form = Chair_Specs()

            context = {
                "form": form,
            }

            return render(request, "app1/chair_specs.html", context)

        elif request.session['product_type'] == "8":
            form = Mattress_Specs()

            context = {
                "form": form,
            }

            return render(request, "app1/mattress_specs.html", context)

        elif request.session['product_type'] == "7":
            form = Bed_Specs()

            context = {
                "form": form,
            }

            return render(request, "app1/bed_specs.html", context)

        elif request.session['product_type'] == "6":
            form = Stove_Specs()

            context = {
                "form": form,
            }

            return render(request, "app1/stove_specs.html", context)

        elif request.session['product_type'] == "5":
            pass

        elif request.session['product_type'] == "4":
            form = Fridge_Specs()

            context = {
                "form": form,
            }

            return render(request, "app1/fridge_specs.html", context)

        elif request.session['product_type'] == "3":
            form = Almirah_Specs()

            context = {
                "form": form,
            }

            return render(request, "app1/almirah_specs.html", context)

        elif request.session['product_type'] == "2":
            pass

        elif request.session['product_type'] == "1":
            pass

        else:
            return render(request, "app1/contact_page.html")

def verify_mail(request):
    '''
    string = ""
    lst = []
    email = request.session['email']

    for word in email:
        if word != "@":
            lst.append(word)
        else:
            break

    if len(lst) > 5:
        string += lst[3]
        string += lst[1]
        string += lst[2]
        string += lst[4]

    if len(lst) < 4:
        if len(lst) == 3:
            string += last[1]
            string += lst[0]
            string += "2"
            string += lst[2]

        if len(lst) == 2:
            string += lst[1]
            string += lst[0]
            string += "8"
            string += lst[0]

        if len(lst) == 1:
            string += lst[0]
            string += "4"
            string += lst[0]
            string += "9"
    '''

    if request.method == "POST":

        form = Verify_Email(request.POST)
        if form.is_valid():
            user = user_info.objects.get(username=request.session["username"],
                                         password=request.session["password"])
            if user.mail_otp == form.cleaned_data['otp']:
                user.mail_otp = ""
                user.mail_verified = True
                user.save()
                return redirect(reverse("user_details"))

            else:
                pass

            '''
            with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", 'r', encoding='utf-8') as f:
                for line in f:
                    email = line[5:]
                    if request.session['email'] == email:
                        otp = line[:4]
                        if otp == form.cleaned_data['otp']:
                            user = user_info.objects.filter(username=form.cleaned_data['username'],
                                                       password=form.cleaned_data['password'])
                            user.mail_verified = True
                            user.save()

                            with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", "r") as f:
                                lines = f.readlines()
                            with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", "w") as f:
                                for line in lines:
                                    if line != f"{otp}:{request.session['email']}":
                                        f.write(line)
                            return redirect(reverse("user_details"))

                        else:
                            pass
            '''

    else:
        string = ""
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        l = []
        for i in range(4):
            num = random.choice(lst)
            l.append(num)

        for ele in l:
            string += str(ele)

        user = user_info.objects.get(username=request.session["username"],
                                     password=request.session["password"])

        user.mail_otp = string
        user.save()

        '''
        with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", 'w', encoding='utf-8') as f:
            f.write(f"{string}:{request.session['email']}")
        '''

        subject = 'OTP Verification'
        message = f'Your OTP is: {string}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.session['email'], ]
        send_mail(subject, message, email_from, recipient_list)

        form = Verify_Email()
        context = {
            "form": form,
        }

        return render(request, "app1/mail_verify.html", context)


def verify_number(request):
    if request.method == "POST":
        form = Verify_Mobile(request.POST)

        if form.is_valid():
            user = user_info.objects.get(username=request.session["username"],
                                         password=request.session["password"])
            request.session['tele'] = form.cleaned_data['number']

            string = ""
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            l = []
            for i in range(4):
                num = random.choice(lst)
                l.append(num)

            for ele in l:
                string += str(ele)

            subject = 'OTP Verification'
            message = f"Number:{request.session['tele']}, otp:{string}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["yashd026@gmail.com", ]
            send_mail(subject, message, email_from, recipient_list)

            user.number = form.cleaned_data['number']
            user.otp_sent = True
            user.num_otp = string
            user.save()

            return redirect(reverse("verify_Num"))

    else:
        form = Verify_Mobile()

    context = {
        "form": form,
    }

    return render(request, "app1/num_verify.html", context)


def Verify_Mail(request):
    '''
    string = ""
    lst = []
    email = request.session['email']

    for word in email:
        if word != "@":
            lst.append(word)
        else:
            break

    if len(lst) > 5:
        string += lst[3]
        string += lst[1]
        string += lst[2]
        string += lst[4]

    if len(lst) < 4:
        if len(lst) == 3:
            string += last[1]
            string += lst[0]
            string += "2"
            string += lst[2]

        if len(lst) == 2:
            string += lst[1]
            string += lst[0]
            string += "8"
            string += lst[0]

        if len(lst) == 1:
            string += lst[0]
            string += "4"
            string += lst[0]
            string += "9"
    '''

    if request.method == "POST":

        form = Verify_Email(request.POST)
        if form.is_valid():
            user = seller_info.objects.get(username=request.session["username"],
                                           password=request.session["password"])
            if user.mail_otp == form.cleaned_data['otp']:
                user.mail_otp = ""
                user.mail_verified = True
                user.save()

                return redirect(reverse("Num_Verify"))
                # return redirect(reverse("seller_details"))

            else:
                pass

            '''
            with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", 'r', encoding='utf-8') as f:
                for line in f:
                    email = line[5:]
                    if request.session['email'] == email:
                        otp = line[:4]
                        if otp == form.cleaned_data['otp']:
                            user = user_info.objects.filter(username=form.cleaned_data['username'],
                                                       password=form.cleaned_data['password'])
                            user.mail_verified = True
                            user.save()

                            with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", "r") as f:
                                lines = f.readlines()
                            with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", "w") as f:
                                for line in lines:
                                    if line != f"{otp}:{request.session['email']}":
                                        f.write(line)
                            return redirect(reverse("user_details"))

                        else:
                            pass
            '''

    else:
        string = ""
        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        l = []
        for i in range(4):
            num = random.choice(lst)
            l.append(num)

        for ele in l:
            string += str(ele)

        user = seller_info.objects.get(username=request.session["username"],
                                       password=request.session["password"])

        user.mail_otp = string
        user.save()

        '''
        with open("C:/Users/My PC/Desktop/web projects/rentite/rentite/my_site/templates/my_site/otp.txt", 'w', encoding='utf-8') as f:
            f.write(f"{string}:{request.session['email']}")
        '''

        subject = 'OTP Verification'
        message = f'Your OTP is: {string}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [request.session['email'], ]
        send_mail(subject, message, email_from, recipient_list)

        form = Verify_Email()
        context = {
            "form": form,
        }

        return render(request, "app1/mail_verify.html", context)


def Verify_Number(request):
    if request.method == "POST":
        form = Verify_Mobile(request.POST)

        if form.is_valid():
            user = seller_info.objects.get(username=request.session["username"],
                                           password=request.session["password"])
            request.session['tele'] = form.cleaned_data['number']

            string = ""
            lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
            l = []
            for i in range(4):
                num = random.choice(lst)
                l.append(num)

            for ele in l:
                string += str(ele)

            subject = 'OTP Verification'
            message = f"Number:{request.session['tele']}, otp:{string}"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ["yashd026@gmail.com", ]
            send_mail(subject, message, email_from, recipient_list)

            user.number = form.cleaned_data['number']
            user.otp_sent = True
            user.num_otp = string
            user.save()

            return redirect(reverse("Verify_Num"))

    else:
        form = Verify_Mobile()

    context = {
        "form": form,
    }

    return render(request, "app1/num_verify.html", context)


def Verify_Num(request):
    if request.method == "POST":
        form = Verify_Email(request.POST)

        if form.is_valid():
            user = seller_info.objects.get(username=request.session["username"],
                                           password=request.session["password"])
            if form.cleaned_data['otp'] == user.num_otp:
                user.number = request.session['tele']
                user.num_verified = True
                user.otp_sent = False
                user.num_otp = ""
                user.save()

                return redirect(reverse("seller_details"))

            else:
                pass

    else:
        form = Verify_Email()

    context = {
        "form": form,
    }

    return render(request, "app1/mail_verify.html", context)


def verify_num(request):
    if request.method == "POST":
        form = Verify_Email(request.POST)

        if form.is_valid():
            user = user_info.objects.get(username=request.session["username"],
                                         password=request.session["password"])
            if form.cleaned_data['otp'] == user.num_otp:
                user.number = request.session['tele']
                
                
                user.num_verified = True
                user.otp_sent = False
                user.num_otp = ""
                user.save()

                return redirect(reverse("user_home"))

            else:
                pass

    else:
        form = Verify_Email()

    context = {
        "form": form,
    }

    return render(request, "app1/mail_verify.html", context)


def num_verify(request):
    user = user_info.objects.get(username=request.session["username"],
                                 password=request.session["password"])
    if user.otp_sent == False:
        return redirect(reverse("Verify_number"))
    else:
        return redirect(reverse("verify_num"))


def Num_Verify(request):
    user = seller_info.objects.get(username=request.session["username"],
                                   password=request.session["password"])
    if user.otp_sent == False:
        return redirect(reverse("Verify_Number"))
    else:
        return redirect(reverse("Verify_Num"))


def filter(request):
    if request.method == "POST":
        if request.session['product_type'] == "1":
            pass

        elif request.session['product_type'] == "2":
            pass

        elif request.session['product_type'] == "3":
            if add_product.objects.filter(product_type = request.session['product_type'], material = form.cleaned_data['material'], drawers = form.cleaned_data['drawers'], color = form.cleaned_data['color'], rent__lt = form.cleaned_data['rent']).exists():
                obj_lst = add_product.objects.filter(product_type = request.session['product_type'], material = form.cleaned_data['material'], drawers = form.cleaned_data['drawers'], color = form.cleaned_data['color'], rent__lt = form.cleaned_data['rent'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass

        elif request.session['product_type'] == "4":
            if add_product.objects.filter(product_type=request.session['product_type'],
                                          color=form.cleaned_data['color'],
                                          rent__lt=form.cleaned_data['rent'], rating = form.cleaned_data['rating'], capacity = form.cleaned_data['capacity'], door = form.cleaned_data['door']).exists():
                obj_lst = add_product.objects.filter(product_type=request.session['product_type'],
                                                     color=form.cleaned_data['color'],
                                                     rent__lt=form.cleaned_data['rent'], rating = form.cleaned_data['rating'], capacity = form.cleaned_data['capacity'], door = form.cleaned_data['door'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass

        elif request.session['product_type'] == "5":
            if add_product.objects.filter(product_type=request.session['product_type'],
                                          color=form.cleaned_data['color'],
                                          rent__lt=form.cleaned_data['rent'], rating = form.cleaned_data['rating'], capacity = form.cleaned_data['capacity']).exists():
                obj_lst = add_product.objects.filter(product_type=request.session['product_type'],
                                                     color=form.cleaned_data['color'],
                                                     rent__lt=form.cleaned_data['rent'], rating = form.cleaned_data['rating'], capacity = form.cleaned_data['capacity'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass

        elif request.session['product_type'] == "6":
            if add_product.objects.filter(product_type = request.session['product_type'], color = form.cleaned_data['color'], rent__lt = form.cleaned_data['rent'], burner = form.cleaned_data['burner'], stove_type = form.cleaned_data['stove_type']).exists():
                obj_lst = add_product.objects.filter(product_type = request.session['product_type'], color = form.cleaned_data['color'], rent__lt = form.cleaned_data['rent'], burner = form.cleaned_data['burner'], stove_type = form.cleaned_data['stove_type'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass

        elif request.session['product_type'] == "7":
            if add_product.objects.filter(product_type = request.session['product_type'], color = form.cleaned_data['color'], rent__lt = form.cleaned_data['rent'], bed_type = form.cleaned_data['bed_type'], storage = form.cleaned_data['storage'], with_mattress = form.cleaned_data['with_mattress']).exists():
                obj_lst = add_product.objects.filter(product_type = request.session['product_type'], color = form.cleaned_data['color'], rent__lt = form.cleaned_data['rent'], bed_type = form.cleaned_data['bed_type'], storage = form.cleaned_data['storage'], with_mattress = form.cleaned_data['with_mattress'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass

        elif request.session['product_type'] == "8":
            if add_product.objects.filter(product_type = request.session['product_type'], rent__lt = form.cleaned_data['rent'], bed_type = form.cleaned_data['bed_type']).exists():
                obj_lst = add_product.objects.filter(product_type = request.session['product_type'], rent__lt = form.cleaned_data['rent'], bed_type = form.cleaned_data['bed_type'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass

        elif request.session['product_type'] == "9":
            if add_product.objects.filter(product_type = request.session['product_type'], rent__lt = form.cleaned_data['rent'], material = form.cleaned_data['material'], armrest = form.cleaned_data['armrest'], foldable = form.cleaned_data['foldable'], pack_of = form.cleaned_data['pack_of']).exists():
                obj_lst = add_product.objects.filter(product_type = request.session['product_type'], rent__lt = form.cleaned_data['rent'], material = form.cleaned_data['material'], armrest = form.cleaned_data['armrest'], foldable = form.cleaned_data['foldable'], pack_of = form.cleaned_data['pack_of'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass

        elif request.session['product_type'] == "10":
            if add_product.objects.filter(product_type = request.session['product_type'], rent__lt = form.cleaned_data['rent'], color = form.cleaned_data['color']).exists():
                obj_lst = add_product.objects.filter(product_type = request.session['product_type'], rent__lt = form.cleaned_data['rent'], color = form.cleaned_data['color'])
                context = {
                    "obj_lst": obj_lst
                }
                return render(request, "app1/product_page.html", context)

            else:
                pass
        
    else:
        if request.session['product_type'] == "1":
            pass
            
        elif request.session['product_type'] == "2":
            pass

        elif request.session['product_type'] == "3":
            form = Almirah_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/almirah_filter.html", context)

        elif request.session['product_type'] == "4":
            form = Fridge_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/fridge_filter.html", context)
            
        elif request.session['product_type'] == "5":
            form = Purifier_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/purifier_filter.html", context)


        elif request.session['product_type'] == "6":
            form = Stove_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/stove_filter.html", context)

        elif request.session['product_type'] == "7":
            form = Bed_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/bed_filter.html", context)
            
        elif request.session['product_type'] == "8":
            form = Mattress_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/mattress_filter.html", context)

        elif request.session['product_type'] == "9":
            form = Chair_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/chair_filter.html", context)

        elif request.session['product_type'] == "10":
            form = Fan_Filter()

            context = {
                "form": form
            }
            return render(request, "app1/fan_filter.html", context)
