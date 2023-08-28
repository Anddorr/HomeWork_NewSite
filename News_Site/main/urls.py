from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('info', views.info),
    path('articles', views.articles),
    path('category/<int:pk>', views.get_exact_category),
    path('articles/<int:pk>', views.get_exact_article),
    path('search', views.search_product),
    path('write-comment/<int:pk>', views.add_comment),
    path('post-comment/<int:pk>', views.post_comment),
    path('add_article', views.add_article),
    path('post_article', views.post_article),
    path('delete_article/<int:pk>', views.delete_article),
    path('edit_article/<int:pk>', views.edit_article),
    path('post_edit_article/<int:pk>', views.post_edit_article)
]