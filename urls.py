"""Все ссылки системы линкера"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name = "index"),
    path('price', views.price, name = "price"),
    path('linker', views.linker, name = "linker"),
    path('linker/url/create', views.generate_url, name="generate_url"),
    path('linker/qr/create', views.generate_qr, name="generate_qr"),
    path('linker/<str:url>', views.linker, name = "linker_with_url"),

    path('urls/title/update', views.update_url_title, name = "update_url_title"),
    path('urls/delete', views.delete_url, name = "delete_url_title"),
    path('urls/history', views.history_urls, name = "history_urls"),

    path('qr', views.qr_generator, name = "qr_generator"),
    path('qr/update', views.update_qr_params, name = "qr_update"),
    path('qr/<str:url>', views.qr_generator, name = "qr_generator"),
    path('qrs/delete', views.delete_qr, name = "delete_qr"),
    path('qrs/history', views.history_qrs, name = "history_qrs"),

    path('<str:url>', views.redirect_to_url, name = "redirect_to_url"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
