from rest_framework import generics

from .serializers import HumanSerializer, FamilyTreeSerializer
from .models import Human


class HumanReadUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer


class HumanCreateView(generics.CreateAPIView):
    queryset = Human.objects.all()
    serializer_class = HumanSerializer


class HumanAncestorsView(generics.RetrieveAPIView):
    queryset = Human.objects.select_related("mother_id", "father_id")
    serializer_class = FamilyTreeSerializer
