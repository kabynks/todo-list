from django.urls import path
from lists.views import home_page, view_list, new_list

urlpatterns = [
    path('new', new_list, name='new_list'),
    path('<int:pk>/', view_list, name='view_list'),
]