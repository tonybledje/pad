from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'padneb'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    path('member_list', views.member_list, name='member_list'),
    path('member/<int:pk>/edit/', views.member_edit, name='member_edit'),
    path('member/create/', views.member_new, name='member_new'),
    path('contribution_list', views.contribution_list, name='contribution_list'),
    path('contribution/<int:pk>/edit/', views.contribution_edit, name='contribution_edit'),
    path('contribution/create/', views.contribution_new, name='contribution_new'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('about', views.about, name='about'),
    ]