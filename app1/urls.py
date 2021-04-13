from django.urls import path, re_path
from . import views
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    re_path(r'^home/$', views.user_home, name="user_home"),
    re_path(r'^sign_up/$', views.user_signup, name="user_sign_up"),
    re_path(r'^details/$', views.user_details, name="user_details"),
    re_path(r'^login/$', views.user_login, name="user_login"),
    re_path(r'^SignUp/$', views.seller_signup, name="seller_sign_up"),
    re_path(r'^Login/$', views.seller_login, name="seller_login"),
    re_path(r'^Details/$', views.seller_details, name="seller_details"),
    re_path(r'^contact/$', views.contact, name="contact"),
    re_path(r'^add_product/$', views.add_products, name="add_product"),
    re_path(r'^my_products/$', views.my_products, name="my_products"),
    re_path(r'^add_specs/$', views.add_specs, name="add_specs"),
    re_path(r'^verify_email/$', views.verify_mail, name="verify_email"),
    re_path(r'^verify_number/$', views.verify_number, name="verify_number"),
    re_path(r'^Verify_Email/$', views.Verify_Mail, name="Verify_Email"),
    re_path(r'^Verify_Number/$', views.Verify_Number, name="Verify_Number"),
    re_path(r'^Verify_Num/$', views.Verify_Num, name="Verify_Num"),
    re_path(r'^verify_num/$', views.verify_num, name="verify_num"),
    re_path(r'^Num_Verify/$', views.Num_Verify, name="Num_Verify"),
    re_path(r'^num_verify/$', views.num_verify, name="num_verify"),
    re_path(r'^filter/$', views.filter, name = "filter"),
    re_path(r'^add_specs1/$', views.add_specs1, name="add_specs1"),
    re_path(r'^almirah/$', views.almirah, name="almirah"),
    re_path(r'^refrigerator/$', views.refrigerator, name="refrigerator"),
    re_path(r'^purifier/$', views.purifier, name="purifier"),
    re_path(r'^stove/$', views.stove, name="stove"),
    re_path(r'^bed/$', views.bed, name="bed"),
    re_path(r'^mattress/$', views.mattress, name="mattress"),
    re_path(r'^chair/$', views.chair, name="chair"),
    re_path(r'^fan/$', views.fan, name="fan"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

'''
    re_path(r'^add_specs2/$', views.add_specs2, name="add_specs2"),
    re_path(r'^add_specs3/$', views.add_specs3, name="add_specs3"),
    re_path(r'^add_specs4/$', views.add_specs4, name="add_specs4"),
    re_path(r'^add_specs5/$', views.add_specs5, name="add_specs5"),
    re_path(r'^add_specs6/$', views.add_specs6, name="add_specs6"),
    re_path(r'^add_specs7/$', views.add_specs7, name="add_specs7"),
    re_path(r'^add_specs8/$', views.add_specs8, name="add_specs8"),
    re_path(r'^add_specs9/$', views.add_specs9, name="add_specs9"),
'''