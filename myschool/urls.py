from django.urls import path
from . import views 
urlpatterns = [
    path("load_data_from_csv/",views.load_data_from_csv,name="visualize_data")
]