from django.urls import path
from . import views

urlpatterns = [
    # trigger projects function when we visit projects/URL
    # This part defines URL patterns specific to the projects app.
    path("projects/", views.projects, name="projects"), # Routed to projects view function.
    path("project/<str:pk>/", views.project, name="project") # Routed to project view function, with the 
                                                            # <str:pk> part capturing a project's primary key (ID) in the URL.
]
