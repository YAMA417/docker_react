# my_api/urls.py
from . import views
from rest_framework import routers
from my_api.viewsets import TaskViewSet
from my_api.viewsets import AcountViewSet

app_name = 'my_api'
router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'acount', AcountViewSet)
