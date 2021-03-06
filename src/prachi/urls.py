"""prachi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from pages.views import home_view,login_view,signup_view,details_view
#from login.views import viewlogin
from detail import views
from django.contrib.auth import views as auth_views
from signup.views import register
urlpatterns = [
    path('',home_view, name='home'),
    path('viewdetail/',views.viewdetail,name='details'),
    path('cv/',views.show),
    path('login/',auth_views.LoginView.as_view(template_name='../templates/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='../templates/logout.html'),name='logout'),
    path('signup/',register,name='signup'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)