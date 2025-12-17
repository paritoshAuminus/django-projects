from django.urls import path
from . import views

urlpatterns = [
    # path('', views.normal, name='normal'),    # testing purpose
    path('set_session/', views.set_session, name='set_session'),
    path('get_session/', views.get_session, name='get_session'),
    path('delete_session/', views.delete_session, name='get_session'),
]
