from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('info', views.info),
    path('articles', views.articles),
    path('category/<int:pk>', views.get_exact_category),
    path('articles/<int:pk>', views.get_exact_article),
]