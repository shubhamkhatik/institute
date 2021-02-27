"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url
from webapp.views import home_page,course_page,thank_page,about_page,services_page,register_page,login_page
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', home_page),
    url(r'^contact/', course_page),
    url(r'^about/', about_page),
    url(r'^services/', services_page),
    url(r'^registration/', register_page),
    url(r'^$', login_page),
    url(r'^thank/',thank_page)
]

