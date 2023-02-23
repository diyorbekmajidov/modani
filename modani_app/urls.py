from django.urls import path
from .views import CatologListView

urlpatterns = [
    path('catologs/', CatologListView.as_view()),
]