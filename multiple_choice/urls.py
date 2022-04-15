from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('new_test', views.new, name="new_test"),
    path('take_test', views.take_test, name="take_test"),
    path('edit_test', views.edit, name="edit_test"),
    path('list', views.edit, name="list"),
    path('account_info', views.account, name="account_info"),
]