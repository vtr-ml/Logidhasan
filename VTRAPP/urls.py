from django.urls import path
from VTRAPP import views


urlpatterns = [
    path('', views.index, name='index'),
    path('Videocall', views.Videocall, name='Videocall'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('resume', views.resume, name='resume'),
    path('services', views.services, name='services'),
    path('skills', views.skills, name='skills'),
    path('Myportfolio', views.Myportfolio, name='Myportfolio'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('reg', views.reg, name='reg'),
    path('register', views.register, name='register.html')

]