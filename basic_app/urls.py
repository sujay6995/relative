from django.conf.urls import url
from basic_app.views import index,other,relative

app_name = 'basic_app'
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^other',other,name='other'),
    url(r'^relative', relative, name='relative'),
]
