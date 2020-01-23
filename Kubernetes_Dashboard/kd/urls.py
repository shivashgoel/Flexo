from django.urls import path
from . import views
urlpatterns = [
    path('', views.kd_home ,name='KD-home'),
    path('pod-list/', views.podlist ,name='KD-Pod-List')
]