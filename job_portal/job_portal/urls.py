"""
URL configuration for job_portal project.

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

from django.conf import settings
from django.conf.urls.static import static
from jobapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('login',views.user_login,name='login'),
    path('registration',views.register,name='registration'),
    path('joblisting',views.joblisting,name='joblisting'),
    path('about',views.about,name='about'),
    path('view_job/<int:jid>',views.view_job,name='view_job'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('postjob',views.postjob,name='postjob'),
    path('save_application/',views.save_application,name='save_application'),
    path('del_save_jobs/<int:job_id>',views.delete_save_job,name='del_save_jobs'),
    path('job_applied',views.job_applied,name='job_applied'),
    path('delete/<int:job_id>',views.del_job_applied,name='del_job_applied'),
    
    path('logout',views.user_logout,name="logout"),
   

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)