# visits/urls.py
from django.urls import path
from .views import RetailPointList, VisitCreate

urlpatterns = [
    path('retail-points/', RetailPointList.as_view(), name='retail-points-list'),
    path('visits/', VisitCreate.as_view(), name='visit-create'),
]
