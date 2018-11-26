from django.conf.urls import url
from django.contrib.auth.views import LoginView
from . import views

LoginView.template_name='users/login.html'
app_name='[users]'

urlpatterns=[
    # 登陆页面
    url(r'^login/$',LoginView.as_view(),name='login'),
    # 注销登陆
    url(r'^logout/$',views.logout_view, name='logout'),
    # 注册页面
    url(r'^register/$',views.register,name='register'),

]