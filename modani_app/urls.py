from django.urls import path
from .views import (
    CatologListView,
    Getcatolog,
    Updatecatolog,
    Deletecatolog,
    SubcategoryListView,
    Subcategoryget,
    Subcatogorydelet,
    UpdateSubcategory,
    ProductListView,
    Productget,
    Productdelet,
    UpdateProduct
)

urlpatterns = [
    path('catologs/', CatologListView.as_view()),
    path('sub_catogry/', SubcategoryListView.as_view()),
    path('sub_catogryget/<int:id>/', Subcategoryget.as_view()),
    path('products/', ProductListView.as_view()),
    path('getproduct/<int:id>/', Productget.as_view()),
    path('getcatolog/', Getcatolog.as_view()),
    path('updatecatolog/<int:id>/', Updatecatolog.as_view()),
    path('deletcatolog/<int:id>/', Deletecatolog.as_view()),
    path('updatesubcatogry/<int:id>/', UpdateSubcategory.as_view()),
    path('deletsubcatogry/<int:id>/', Subcatogorydelet.as_view()),
    path('updateproduct/<int:id>/', UpdateProduct.as_view()),
    path('deletproduct/<int:id>/', Productdelet.as_view()),
]