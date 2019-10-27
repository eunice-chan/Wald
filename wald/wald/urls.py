
from django.contrib import admin
from django.urls import include, path
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('polls/', include('polls.urls')),
    path('time/', view.current_datetime),
    path('home/', view.home),
=======
    path('homepage/', include('homepage.urls')),
>>>>>>> 05be06727ac4bf32d3ce6045466b52e2ea7ba387
]
