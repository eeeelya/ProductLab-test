from django.core.validators import FileExtensionValidator
from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    article_file = serializers.FileField(
        required=False, validators=[FileExtensionValidator(allowed_extensions=["xlsx"])]
    )
    single_article = serializers.CharField(required=False)

    class Meta:
        fields = ["article_file", "single_article"]

    def validate(self, attrs):
        if "article_file" in attrs and "single_article" in attrs:
            raise serializers.ValidationError("You can input only 1 item (article or file).")

        return attrs
