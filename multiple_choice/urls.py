from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name="login"),
    path('signup', views.signup, name="signup"),
    path('new_test', views.new_test, name="new_test"),
    path('take_test', views.take_test, name="take_test"),
    path('logout', views.logout, name="logout"),
    path('new_test', views.new_test, name="new_test"),
    path('edit_test', views.edit, name="edit_test"),
    path('list', views.list, name="list"),
    path('account_info', views.account, name="account_info"),
    path('add_questions', views.add_questions, name= "add_questions"),
    path('possible_tests', views.possible_tests, name="possible_tests"),
    path('take_test/<int:test_id>', views.take_test, name="take_test"),
    path('test_taken/<int:test_id>', views.test_taken, name="test_taken"),
    path('questions', views.questions, name="questions"),


]