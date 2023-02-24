from django.urls import path
from .views import CatologListView,SubcategoryListView

urlpatterns = [
    path('catologs/', CatologListView.as_view()),
    path('sub_catogry/', SubcategoryListView.as_view())
]