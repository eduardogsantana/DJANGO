from django.urls import path
from .views import index,delete_comida

urlpatterns = [
    path('', index, name='index' ),
    path('delete/<int:id>', delete_comida, name='delete'),
]
