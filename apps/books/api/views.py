from apps.books.models import Book
from drf_haystack.filters import HaystackFilter
from drf_haystack.viewsets import HaystackViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from .serializers import BookHaystackSerializer, BookSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = []


class BookHaystackView(HaystackViewSet):
    index_models = [Book]
    serializer_class = BookHaystackSerializer
    filter_backends = [HaystackFilter, OrderingFilter]
    ordering_fields = ["title"]
