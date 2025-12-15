from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'collections', views.CollectionViewSet)

reviews_router = router.NestedSimpleRouter(router, r'products', lookup_value='product')
reviews_router.register(r'reviews', views.ReviewViewSet)

urlpatterns = router.urls + reviews_router.urls
