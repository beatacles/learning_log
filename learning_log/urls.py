from django.contrib import admin
from django.urls import path, include

app_name = 'learning_logs'
urlpatterns = [
    # Домашняя страница
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('learning_logs.urls')),
]
