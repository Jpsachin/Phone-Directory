from django.conf.urls import url
from . import templates, views

urlpatterns =[
    url(r'^$', views.hello, name='hello'),
    url(r'^signup/', views.SignUpFormView.as_view(), name='signup'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^adminsignin/', views.adminsignin, name='adminsignin'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^Admindashboard/', views.AdminUpdate, name='Admindashboard'),
    url(r'^userupdate/', views.userupdate, name='userupdate'),
    url(r'^Administratore/', views.Administratore, name='Administratore'),
    url(r'^AdminUpdate/', views.AdminUpdate, name='AdminUpdate'),
    #url(r'^subscriber/', views.subscriber, name='subscriber'),
#url(r'^signout/', views.signout, name='signout'),
]