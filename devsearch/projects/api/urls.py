from django.urls import path
from . import views
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('projects/', views.project_list),
    path('projects/<int:id>', views.project_detail)
]

# post_router = DefaultRouter()
# post_router.register(r'projects', views.project_list, basename='project')

'''
Registers the ProjectViewSet with the router, specifying the base URL prefix 'projects'. 
So all endpoints for the ProjectViewSet will be prefixed with /projects/.
Using DefaultRouter in DRF automatically generates URL patterns for the standard set of CRUD 
operations (list, retrieve, create, update, delete) for the ProjectViewSet. 
These URL patterns are then included in the main URL configuration of your project, 
allowing you to access the API endpoints provided by the viewset.
'''