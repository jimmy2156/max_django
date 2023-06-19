from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:month>", views.monthly_challenges, name="number_challenge"),
    path("<int:month_int>", views.monthly_challenges_by_number)
] 