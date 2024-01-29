
from django.contrib import admin
from django.urls import path
from countgame.views import allgames, nowa, Nposition

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Gry', allgames),
    path('nowaGra', nowa),
    path('Dodaj',Nposition)

]
