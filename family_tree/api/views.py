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
    queryset = Human.objects.all()
    serializer_class = FamilyTreeSerializer

    # update context with depth parameter
    def get_serializer_context(self):
        context = super().get_serializer_context()
        depth = 0
        try:
            depth = int(self.request.query_params.get("depth", 0))
        except ValueError:
            pass  # Ignore non-numeric parameters and keep default 0 depth

        context["depth"] = depth
        print("context depth", context["depth"])
        return context
