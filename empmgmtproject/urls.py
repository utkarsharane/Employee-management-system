"""
URL configuration for empmgmtproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from empmgmtapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('employee_detail/<int:employee_id>',views.employee_detail,name='employee_detail'),
    path('salary_report', views.salary_report, name='salary_report'),
    path('add_salary/<int:employee_id>/', views.add_salary, name='add_salary'),
    path('update_salary/<int:salary_id>/', views.update_salary, name='update_salary'),
    path('delete_salary/<int:salary_id>/', views.delete_salary, name='delete_salary'),
    
]
