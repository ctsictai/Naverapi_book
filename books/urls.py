from django.conf.urls import url
from . import views

app_name = 'books'

urlpatterns = [
    url(r'^$', views.index),
    url(r'^booksearch/$', views.booksearch, name='api_booksearch'),
    # name은 view이름 식별하는 인자 movieapi에서 이미 api_search를
    # 사용했기 때문에 이름을 바꿈
]
