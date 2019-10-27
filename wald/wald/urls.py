
from django.contrib import admin
from django.urls import include, path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', include('homepage.urls'))
]
