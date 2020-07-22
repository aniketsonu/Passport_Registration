from django.conf import settings
from django.conf.urls.static import static

from .views import login_view, registration_view, logout_view, dashboard
from django.urls import path

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='home'),
    path('register/', registration_view, name='register'),
    path('logout/', logout_view, name="logout"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
