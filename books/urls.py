from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'books'

urlpatterns = [
    # /
    url(r'^$', views.index),
    # /book/
    path('book/', views.BookList.as_view(), name='book_list'),
    # /author/
    path('author/', views.AuthorList.as_view(), name='author_list'),
    # /publisher/
    path('publisher/', views.PublisherList.as_view(), name='publisher_list'),
    # /booksearch - naverapi
    url(r'^booksearch/$', views.booksearch, name='api_booksearch'),
    # name은 view이름 식별하는 인자

]
