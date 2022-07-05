import copy

from rest_framework import serializers


# custom alternative to djangorestframework_recursive
# adding dynamic depth management
class RecursiveField(serializers.Serializer):
    def __init__(self, **kwargs):
        self._recurse_basic = kwargs.pop("basic_serializer", None)
        super(RecursiveField, self).__init__(**kwargs)

    def to_representation(self, value):
        cur_depth = self.context.get("depth", 0) - 1
        if cur_depth > 0:
            serializer = self.parent.__class__(value, context={"depth": cur_depth})

        else:
            serializer = self._recurse_basic(value, context={"depth": cur_depth})
        return serializer.data
