from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('goal/<int:user_id>', views.get_goal, name='goal'),
    path('expenses/', views.get_expenses, name='expenses'),

]