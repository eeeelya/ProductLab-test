from django.core.validators import FileExtensionValidator
from rest_framework import serializers


class InputFileSerializer(serializers.Serializer):
    article_file = serializers.FileField(
        required=True, validators=[FileExtensionValidator(allowed_extensions=["xlsx"])]
    )

    class Meta:
        fields = ["article_file"]


class InputArticleSerializer(serializers.Serializer):
    article = serializers.CharField(required=True)

    class Meta:
        fields = ["article"]
