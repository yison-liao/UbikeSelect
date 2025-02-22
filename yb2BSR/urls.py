"""
URL configuration for yb2BSR project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from web import views as web_views




urlpatterns = [
    path("admin/", admin.site.urls),
    path("", web_views.home, name="home"),
    path("login", web_views.home, name="home"),
    path("stations/", web_views.stations, name="stations"),
    path("analysis/", web_views.analysis_view, name="analysis"),
    path(
        "analysis/<str:station_name>/",
        web_views.station_analysis_view,
        name="station_analysis",
    ),
    path("about_us/", include("aboutUS.urls")),
    path("map/", include("mapAPP.urls")),
    # path('404/',web_views.custom_404),
    # path('404/', web_views.custom_404, name='custom_404'),
    
]
handler404 = web_views.custom_404
# 將自定義 404 視圖與指定路徑關聯
# urlpatterns += [
#     path('404/',web_views.custom_404),
# ]