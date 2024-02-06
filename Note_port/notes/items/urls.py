from django.urls import path 
from . import views

app_name = 'items'

urlpatterns = [
    path('mynotes/', views.view_notes, name= 'user_notes'),
    path('create/', views.new_notes, name= 'create'),
    path('mynotes/<int:id>/', views.notes_details, name= 'details'),
    
]