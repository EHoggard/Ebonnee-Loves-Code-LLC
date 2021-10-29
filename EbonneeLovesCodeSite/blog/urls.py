from django.urls import path
# from .views import
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('work/', views.work, name='work'),
    path('single_post/<int:id>/', views.single_post, name='single-post'),
    path('index/', views.index, name='home'),
]