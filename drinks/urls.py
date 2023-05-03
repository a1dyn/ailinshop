from django.urls import path
from .views import DrinkPage, purchase, Success

urlpatterns = [
    path('', DrinkPage.as_view(), name = 'drinks'),
    path('buy/<int:drink_id>', purchase, name='purchase'),
    path('success/', Success.as_view(), name= 'success')
    ]