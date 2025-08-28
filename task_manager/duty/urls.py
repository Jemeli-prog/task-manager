from django.urls import path
from .views import DutyListCreate,DutyDetail

urlpatterns = [
    path('duty/', DutyListCreate.as_view(),name='duty-list-create'),
    path('duty/<int:pk>/', DutyDetail.as_view(), name='duty-detail'),

]
    

