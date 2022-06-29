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


class FamilyTreeSerializer(serializers.ModelSerializer):
    father = RecursiveField(source="father_id")
    mother = RecursiveField(source="mother_id")

    class Meta:
        model = Human
        fields = (
            "id",
            "first_name",
            "last_name",
            "mother",
            "father",
        )


# class AncestorsSerializer(serializers.ModelSerializer):
#     father = serializers.PrimaryKeyRelatedField(read_only=True)
#     mother = serializers.PrimaryKeyRelatedField(read_only=True)

#     class Meta:
#         model = Human
#         fields = (
#             "mother",
#             "father",
#         )
