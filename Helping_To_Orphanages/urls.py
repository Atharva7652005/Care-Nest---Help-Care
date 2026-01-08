"""
URL configuration for Helping_To_Orphanages project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Login.views import *;
from Home.views import *;

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name="Home"),
    path('login/',Login, name="Login"),
    path('logout/',logout_page,name="logout_page"),

    path('feedback/',Feedback,name="Feedback"),
    path('add_orpho/',Add_Orpho,name="Add_Orpho"),
    path('orpho_desc/<id>/',Orpho_Desc,name="Orpho_Desc"),
    path('update_orpho',Update_Orpho,name="Update_Orpho"),
    path('feedback_details',Feedback_Details,name="Feedback_Details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

