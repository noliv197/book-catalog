from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout, name='logout'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/authors', views.authors, name='authors'),
    path('catalog/book_detail/<int:id>', views.book_detail, name='book_detail'),
    path('catalog/author_detail/<int:id>', views.author_detail, name='author_detail'),

]