from django.urls import path
from .views import *

urlpatterns = [
    path('home',CBView.as_view()),
    path('',CBTemplateView.as_view()),
    path('schoollist',SchoolListView.as_view(),name = 'list'),
    path('school/<int:pk>/',SchoolDetailView.as_view(),name = 'detail'),
    path('create/',SchoolCreateView.as_view(),name = 'create'),
    path('update/<int:pk>',SchoolUpdateView.as_view(),name = 'update'),
    path('delete/<int:pk>',SchoolDeleteView.as_view(),name = 'delete'),

]