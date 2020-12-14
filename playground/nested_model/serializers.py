from .models import Annotation, Obstacle, Point, Polygon
from rest_framework import serializers


class ObstacleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Obstacle
        fields = ['polygons']


class AnnotationSerializer(serializers.ModelSerializer):
    obstacles = ObstacleSerializer(many=True)

    class Meta:
        model = Annotation
        fields = ['obstacles', 'name']


class PolygonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Polygon
        field = ['id']


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        field = ['id']