from rest_framework import serializers

class HelloSerialzier(serializers.Serializer):
    """Serialziers a name field for testing our APIView"""
    name = serializers.CharField(max_length= 10)
    