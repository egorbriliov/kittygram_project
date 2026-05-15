"""Вьюхи под API."""

from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Вьюсет под котика."""

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
