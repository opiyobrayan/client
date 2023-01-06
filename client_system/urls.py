
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name='home'),
    path('engagement-form',views.entry, name='engagement-form'),
    path('detail-form',views.client_detail,name='detail-form'),
    path('forms',views.forms,name='forms'),
    path('engaged-clients', views.engaged_clients,name='engaged-clients'),
    path('client/<int:pk>', views.client,name='client'),

]
