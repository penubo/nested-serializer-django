from .models import Annotation, Obstacle, Point
from rest_framework import serializers


class PointSerializer(serializers.ModelSerializer):

    class Meta:
        model = Point
        fields = ['x', 'y']


class ObstacleSerializer(serializers.ModelSerializer):
    polygon = PointSerializer(many=True)

    class Meta:
        model = Obstacle
        fields = ['polygon']


class AnnotationSerializer(serializers.ModelSerializer):
    obstacles = ObstacleSerializer(many=True)

    class Meta:
        model = Annotation
        fields = ['obstacles']

    def create(self, validated_data):
        obstacles_data = validated_data.pop('obstacles')
        annotation = Annotation.objects.create(**validated_data)
        for obstacle_data in obstacles_data:
            points_data = obstacle_data.pop('polygon')
            obstacle = Obstacle.objects.create(annotation=annotation,
                                               **obstacle_data)
            for point_data in points_data:
                Point.objects.create(obstacle=obstacle, **point_data)

        return annotation