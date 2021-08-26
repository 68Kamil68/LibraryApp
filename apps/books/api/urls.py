from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import BookHaystackView, BookViewSet

router = DefaultRouter()
router.register("search", BookHaystackView, basename="book-search")
router.register("", BookViewSet, basename="book")

urlpatterns = [path("", include(router.urls))]
