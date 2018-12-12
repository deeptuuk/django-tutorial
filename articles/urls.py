from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.article_list,name="list"),
    path('<slug>/', views.article_detail,name="detail"),
]
