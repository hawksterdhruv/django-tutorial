"""read URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles import views

from read.views import helloWorld
from reading.views import heatmap_data
from reading.views import write_form
from reading.views import read_list
from reading.views import read_form
from reading.views import read_detail

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', helloWorld),
    url(r'^heatmap_data/', heatmap_data),
    # url(r'^time/plus/(\d{1,2})/',timePlus),
    url(r'^read/list/', read_list),
    url(r'^read/entry/', read_form),
    url(r'^write/', write_form),
    # url(r'^static/(?P<path>.*)$', views.serve),
    url(r'^read/detail/(?P<id>\d+)$', read_detail, name='detail')
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
