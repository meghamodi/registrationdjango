from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views 

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),

]