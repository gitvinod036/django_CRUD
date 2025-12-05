from django.urls import path
from . import views

urlpatterns=[
    path("reg_user/",view=views.reg_user),
    path("get_user/<int:id>",view=views.get_user),
    path("get_user/",view=views.get_user),
    path("update_user/<int:id>",view=views.update_user),
    path("delete_user/<int:id>",view=views.delete_user),
    path("show/",view=views.show),
    path("reg_form/",view=views.reg_form),
    path("update_form/<int:id>",view=views.update_form),
    path("",view=views.homepage)
     
]