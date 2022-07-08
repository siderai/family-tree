from rest_framework import serializers

from .fields import RecursiveField
from .models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = ("id", "first_name", "last_name", "mother_id", "father_id")


class AncestorsDummySerializer(serializers.Serializer):
    id = serializers.IntegerField
    first_name = serializers.CharField
    last_name = serializers.CharField
    mother = serializers.PrimaryKeyRelatedField(read_only=True)
    father = serializers.PrimaryKeyRelatedField(read_only=True)


class DynamicDepthSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.Meta.depth = self.context.get("depth", 10)


class AncestorsSerializer(DynamicDepthSerializer):

    father = RecursiveField(
        source="father_id",
        allow_null=True,
        read_only=True,
        basic_serializer=AncestorsDummySerializer,
    )
    mother = RecursiveField(
        source="mother_id",
        allow_null=True,
        read_only=True,
        basic_serializer=AncestorsDummySerializer,
    )

    class Meta:
        model = Human
        fields = ("id", "first_name", "last_name", "mother", "father")


class FamilyTreeSerializer(DynamicDepthSerializer):
    father = AncestorsSerializer(source="father_id", required=False)
    mother = AncestorsSerializer(source="mother_id", required=False)

    class Meta:
        model = Human
        fields = ("mother", "father")
