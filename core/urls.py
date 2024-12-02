from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from apps.common import views

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    # # path('product-create/',views.ProductCreateAPIView.as_view()),
    # path('product-detail/<int:pk>',views.ProductDetailAPIView.as_view()),
    # path('banner/',views.BannerAPIView.as_view()),
    # path('category/',views.CategoryAPIView.as_view()),
    # path('image/',views.ProductImageAPIView.as_view()),
    # path('product-category/',views.ProductsCategoryAPIView.as_view()),
    # path('catalog/',views.CatalogAPIView.as_view()),
    # path('product-list/', views.ProductListView.as_view()),
    # path('order-create/', views.OrderCreateAPIView.as_view()),
    # path('order-product-create/', views.OrderItemCreateView.as_view()),
    
]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
