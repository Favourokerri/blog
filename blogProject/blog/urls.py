from django.urls import path
from blog import views
urlpatterns = [
    path('', views.home, name="home"),
    path('blogpost/<int:id>/', views.SingleBlogPost, name="singleblogpost"),
    path('newsletter', views.newsletter, name="subscribe"),
    path('search', views.search, name='search'),
    path('comment/<int:id>/', views.comment, name='comment'),
]