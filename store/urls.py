from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'collections', views.CollectionViewSet)

urlpatterns = router.urls
