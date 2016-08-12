from django.conf.urls import url
from django.shortcuts import redirect
from django.contrib.auth.views import login
from blog.templates import blog
from . import views

urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', login, name='login', kwargs={
        'template_name' : 'accounts/login.html', #장고 도큐먼트안에 있는 attribute dict값에서 key를 이용해서 url 접근 값을 변경.
        })
    url()
]