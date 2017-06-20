from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search_results/$', views.search_results, name='search_results'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^admin_actions/$', views.admin_actions, name='admin_actions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
