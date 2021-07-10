from django.urls import path, include 
from rest_framework.routers import DefaultRouter

from . import views
router = DefaultRouter()
router.register('',views.ProductViewSet,basename='')

urlpatterns =[
    # path('latest-product/', views.LatestProductList.as_view()),
    path('product/search/', views.search),
    path('latest-product/',include(router.urls)),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view())
]