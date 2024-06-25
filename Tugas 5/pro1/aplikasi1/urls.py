"""URL configuration for FirstApp project.The `urlpatterns` list routes URLs to views. 
For more information please see:    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:Function views    1. Add an import:  from my_app import views   
 2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views    1. Add an import:  from other_app.views import Home   
 2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf    1. Import the include() function: from django.urls 
import include, path    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))"""

from django.urls import path
from aplikasi1 import views



app_name = 'aplikasi1'
urlpatterns = [
    path('', views.readStudent, name='read-data-student'),   
    path('create/', views.createStudent, name='create-data-student'),   
    path('update/<str:id>', views.updateStudent, name='update-data-student'),   
    path('delete/<str:id>', views.deleteStudent, name='delete-data-student')
]