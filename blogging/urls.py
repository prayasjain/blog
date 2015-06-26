from django.conf.urls import patterns, url
from blogging import views
urlpatterns = patterns('',
                       url(r'^$',views.mainpage,name='main'),
                       url(r'^home/(?P<user_name_slug>[\w\-]+)/$',views.home,name='home'),
                        


                       )