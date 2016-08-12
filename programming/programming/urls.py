"""programming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from blog import views
from posting_hw import views as posting_hw_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.post_list),
    url(r'^comments/new/$', views.comment_new),
    url(r'', include('posting_hw.urls', namespace='posting')),
    url(r'', include('poketmon.urls', namespace='poketmon')),
    url(r'^accounts/', include('accounts.urls')), #account가 auth를 참조할 거기 때문에 namespace를 지정하지 않는다.
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)