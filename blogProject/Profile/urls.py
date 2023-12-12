from django.urls import path
from Profile import views
urlpatterns = [
    path('contact_us', views.contact, name="contact"),
    path('about_us', views.about, name="about"),
    path('log_in', views.log_in, name="login"),
    path('logout/', views.log_out, name='logout'),
    
]