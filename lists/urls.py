from django.urls import path
from lists.views import home_page, view_list, new_list, add_item

urlpatterns = [
    path('new', new_list, name='new_list'),
    path('<int:pk>/', view_list, name='view_list'),
    path('<int:pk>/add_item/', add_item, name='add_item')
]