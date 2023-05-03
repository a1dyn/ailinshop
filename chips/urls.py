from django.urls import path
from .views import ChipsPage, purchase, success

urlpatterns = [
    path('', ChipsPage.as_view(), name = 'chips'),
    path('buy/<int:chips_id>', purchase, name='purchase'),
    path('success/', success, name= 'success')
    ]