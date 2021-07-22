from django.urls import path
from . import views
from .views import Register, CartListView, CreateGroceryListView, UpdateGroceryListView, DeleteGroceryListView, CartLogin, CartLogout
urlpatterns = [
    path('', CartListView.as_view(),name='index'),
    path('addlist',CreateGroceryListView.as_view(),name='add'),
    path('updatelist/<str:pk>/', UpdateGroceryListView.as_view(), name='update'),
    path('deletelist/<str:pk>/', DeleteGroceryListView.as_view(), name='delete'),
    path('login/',CartLogin.as_view(),name ='login'),
    path('logout/', CartLogout.as_view(), name='logout'),
    path('register/',Register.as_view(),name='register')
]
