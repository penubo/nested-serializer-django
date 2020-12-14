from .models import Annotation, Obstacle, Point
from rest_framework import serializers


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = ['x', 'y']


class ObstacleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Obstacle
        fields = ['points']

    def to_representation(self, instance: Obstacle):
        response = super().to_representation(instance)
        response = {"polygon": PointSerializer(instance.points, many=True).data}
        return response


class AnnotationSerializer(serializers.ModelSerializer):
    obstacles = ObstacleSerializer(many=True)

    class Meta:
        model = Annotation
        fields = ['obstacles']
