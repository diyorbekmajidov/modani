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
    UpdateProduct,
    SubCategory,
    SaleListView,
    SaleListUpdate,
    SalelistDelet,
    CartListView,
    CartListUpdate,
    CartListDelet,
    CartGet,
    LikeListView,
    LikeListUpdate,
    LikelistDelet,
    LikeGet,
    SaleListGet,
    SaleGETAll,
    SearchView
)

urlpatterns = [
    path('catologs/', CatologListView.as_view()),
    path('getcatolog/', Getcatolog.as_view()),
    path('deletcatolog/<int:id>/', Deletecatolog.as_view()),
    path('updatecatolog/<int:id>/', Updatecatolog.as_view()),

    path('sub_catogry/', SubcategoryListView.as_view()),
    path('updatesubcatogry/<int:id>/', UpdateSubcategory.as_view()),
    path('deletsubcatogry/<int:id>/', Subcatogorydelet.as_view()),
    path('sub_catogryget/<int:id>/', Subcategoryget.as_view()),

    path('products/', ProductListView.as_view()),
    path('getproduct/<int:id>/', Productget.as_view()),
    path('updateproduct/<int:id>/', UpdateProduct.as_view()),
    path('deletproduct/<int:id>/', Productdelet.as_view()),

    path('subcatogry/<int:pk>/', SubCategory.as_view()),

    path('saleget/<int:id>/', SaleListGet.as_view()),
    path('sale/', SaleListView.as_view()),
    path('saleupdate/<int:id>/', SaleListUpdate.as_view()),
    path('saledelet/<int:id>/', SalelistDelet.as_view()),

    path('cart/', CartListView.as_view()),
    path('cartupdate/<int:id>/', CartListUpdate.as_view()),
    path('cartdelet/<int:id>/', CartListDelet.as_view()),
    path('cartget/<int:id>/', CartGet.as_view()),

    path('like/', LikeListView.as_view()),
    path('likeupdate/<int:id>/', LikeListUpdate.as_view()),
    path('likedelet/<int:id>/', LikelistDelet.as_view()),
    path('likeget/<int:id>/', LikeGet.as_view()),

    path('search/', SearchView.as_view()),
    path('saleget/', SaleGETAll.as_view())
]