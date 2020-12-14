from unittest.case import skip
from .serializers import AnnotationSerializer, ObstacleSerializer, PointSerializer
from .models import Annotation, Obstacle, Point
from django.test import TestCase
from django.forms.models import model_to_dict
import json

# Create your tests here.


class AnnotationModelTest(TestCase):

    def setUp(self):
        pass

    def test_annotation_creation(self):
        annotation = Annotation.objects.create(name='yongjoon')
        self.assertEqual(annotation.name, 'yongjoon')

    def test_annotation_has_related_obstacles_field(self):
        annotation = Annotation.objects.create(name='yongjoon')
        Obstacle.objects.create(annotation=annotation)
        Obstacle.objects.create(annotation=annotation)
        self.assertEqual(annotation.obstacles.count(), 2)


class ObstacleModelTest(TestCase):

    def setUp(self):
        pass

    def test_obstacle_has_polygon_field(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        Point.objects.create(obstacle=obstacle, x=10, y=10)
        self.assertEqual(obstacle.polygon.count(), 1)


class AnnotationSerializerTest(TestCase):

    def setUp(self):
        pass

    def test_annotation_serialized_to_array_of_obstacles(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        Obstacle.objects.create(annotation=annotation)

        Point.objects.create(obstacle=obstacle, x=10, y=10)
        Point.objects.create(obstacle=obstacle, x=20, y=20)

        serializer = AnnotationSerializer(annotation)
        self.assertEqual(len(serializer.data.get('obstacles')), 2)

    def test_create_annotation_with_serializer(self):
        data = {"obstacles": [{"polygon": [{"x": 10, "y": 10}]}]}
        serializer = AnnotationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            obstacle = serializer.data.get('obstacles')[0]
            points = obstacle.get('polygon')[0]
            x, y = points
            self.assertTrue(x, 10)
            self.assertTrue(y, 10)
        else:
            self.fail('annotation should be created by serializer')

    def test_create_annotation_with_multiple_obstacles_with_serializer(self):
        data = {  # annotation
            "obstacles": [
                {  # obstacle1
                    "polygon": [{  # points1
                        "x": 10,
                        "y": 10
                    }]
                },
                {  # obstacle2
                    "polygon": [
                        {  # points2
                            "x": 20,
                            "y": 20
                        },
                        {  # points3
                            "x": 30,
                            "y": 30
                        }
                    ]
                }
            ]
        }
        serializer = AnnotationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            obstacle1, obstacle2 = serializer.data.get('obstacles')
            points1 = obstacle1.get('polygon')[0]
            x, y = points1
            self.assertTrue(x, 10)
            self.assertTrue(y, 10)

            points2, _ = obstacle2.get('polygon')
            x, y = points2
            self.assertTrue(x, 20)
            self.assertTrue(y, 20)
        else:
            self.fail('multiple annotation should be created by serializer')

    def test_create_annotation_without_polygon(self):
        data = {"obstacles": []}
        serializer = AnnotationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            obstacle = serializer.data.get('obstacles')
            self.assertEqual(len(obstacle), 0)
        else:
            self.fail(
                'empty polygon annotation should be created by serializer')


class ObstacleSerializerTest(TestCase):

    def setUp(self):
        pass

    def test_obstacle_serialized_to_polygon(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        Point.objects.create(obstacle=obstacle, x=10, y=10)
        serializer = ObstacleSerializer(obstacle)
        self.assertEqual(len(serializer.data.get('polygon')), 1)

    def test_obstacle_serialized_to_empty_polygon(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        serializer = ObstacleSerializer(obstacle)
        self.assertEqual(len(serializer.data.get('polygon')), 0)
