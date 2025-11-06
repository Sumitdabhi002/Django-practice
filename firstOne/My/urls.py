
from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_my,name='all_home'),
]