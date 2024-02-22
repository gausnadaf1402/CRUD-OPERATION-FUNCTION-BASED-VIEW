from django.urls import path
from . import views

urlpatterns = [
    path('add_student',views.add_student,name='add_student'),
    path('update_student/<int:id>/',views.update_student,name='update_student'),
    path('delete/<int:id>/',views.delete_data,name='delete_data')
]
