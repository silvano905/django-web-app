"""venv_nineteen_dic_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, reverse_lazy
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from app_web import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/$', LoginView.as_view(), {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url(r'^form/$', views.IndexForm.as_view(), name='form'),
    url(r'^$', views.IndexFormTranslate.as_view(), name='translate'),
    url(r'^list/$', views.listwords, name='list'),
    url(r'^list/(?P<pk>\d+)/$', views.WordDetail.as_view(), name='detail'),
    url(r'^create/$', views.createword, name='create'),
    url(r'^delete/(?P<pk>\d+)/$', views.WordDelete.as_view(), name='delete'),
    url(r'^update/(?P<pk>\d+)/$', views.WordUpdate.as_view(), name='update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)