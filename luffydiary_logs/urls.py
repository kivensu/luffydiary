from django.conf.urls import url
from . import views

app_name='[luffydiary_logs]'
urlpatterns =[
    # 主页面
    url(r'^$',views.index, name='index'),
    # 显示所有的主题
    url(r'^topics/$',views.topics, name='topics'),
    # 特定主题的详情页
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    # 添加新主题的网页
    url(r'^new_topic/$', views.new_topic, name='new_topic'),
    # 添加新条目的的页面
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry, name='new_entry'),
    # 编辑现有条目
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry, name='edit_entry'),
]