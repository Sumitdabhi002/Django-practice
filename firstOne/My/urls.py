
from django.urls import path
from . import views
urlpatterns = [
    path('',views.all_my,name='all_home'),
    path('<int:chai_id>/',views.chai_detail,name='chai_details'),
    path('chai_stores/',views.chai_store_view,name='chai_stores'),


]