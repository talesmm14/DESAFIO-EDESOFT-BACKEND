from rest_framework import serializers


class S3Serializer(serializers.Serializer):
    bucket_name = serializers.CharField(max_length=255)
    object_key = serializers.CharField(max_length=255)
