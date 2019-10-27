
from django.contrib import admin
from django.urls import include, path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('time/', view.current_datetime),
    path('home/', view.home),
]
