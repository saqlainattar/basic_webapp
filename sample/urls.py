from django.urls import path
from sample import views

urlpatterns = [
    path("", views.index, name="home"),
    path("employee_details", views.employee_details, name="employee_details"),
    path("contact_us", views.contact_us, name="contact_us"),
    path("accepted", views.accepted, name="accepted"),
    path("rejected", views.rejected, name="rejected"),
]


