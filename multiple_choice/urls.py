from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('logout', views.logout, name="logout"),
    path('menu', views.menu, name="menu"),
    path('add_questions', views.addquestions, name= "add_questions"),

]