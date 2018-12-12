from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.article_list),
    path('<slug>/', view.article_detail),
]
