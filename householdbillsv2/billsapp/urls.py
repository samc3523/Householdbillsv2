
from django.urls import path
from .views import newbill, bills
app_name = "billsapp"
#this where routes are
urlpatterns = [
    path("newbill/", newbill, name="newbill"),
    path("bills/", bills, name="bills"),  
]