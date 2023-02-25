from django.urls import path
from .views import CatologListView,SubcategoryListView,Subcategoryget,ProductListView

urlpatterns = [
    path('catologs/', CatologListView.as_view()),
    path('sub_catogry/', SubcategoryListView.as_view()),
    path('sub_catogryget/<int:id>/', Subcategoryget.as_view()),
    path('products/', ProductListView.as_view()),
]