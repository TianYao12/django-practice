"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls), # Routes requests to the Django admin site.
    path("", include("projects.urls")),  # Routes requests to  projects app by including URLs in projects/urls.py.
    path("api/", include("projects.api.urls")) # Routes requests to devsearch.api app by including URLs in devsearch/api/urls.py.
]
