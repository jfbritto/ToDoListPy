from django.contrib import admin
from django.urls import path, include  # Certifique-se de incluir esta linha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
]
