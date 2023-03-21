from django.urls import path

from apps.api.views import DesafioView

urlpatterns = [
    path('desafio/', DesafioView.as_view())
]
