from django.urls import path
from .views import *

urlpatterns = [
    path('', core, name="core"),
    path('list/', list, name="list"),
    path('list/detail/<int:id>', list_detail, name="detail"),
    path('create/', CharbaCreateView.as_view(), name='create'),
]
