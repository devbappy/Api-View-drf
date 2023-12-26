from django.urls import path
from . import views
from .views import ItemList, ItemDetail, LocationDetail, LocationList

urlpatterns = [
    #path('', views.home, name="home"),
    path('location/', LocationList.as_view()),
    path('location/<int:pk>/', LocationDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
]