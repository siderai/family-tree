from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from .models import Human


class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = (
            "id",
            "first_name",
            "last_name",
            "mother_id",
            "father_id",
        )


class AncestorsSerializer(serializers.ModelSerializer):
    father = RecursiveField(source="father_id", allow_null=True)
    mother = RecursiveField(source="mother_id", allow_null=True)

    class Meta:
        model = Human
        fields = (
            "id",
            "first_name",
            "last_name",
            "mother",
            "father",
        )


class FamilyTreeSerializer(serializers.Serializer):
    father = AncestorsSerializer(source="father_id", required=False)
    mother = AncestorsSerializer(source="mother_id", required=False)
