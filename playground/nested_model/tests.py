from .serializers import AnnotationSerializer
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
        self.assertEqual(annotation.obstacles.count(), 1)


class ObstacleModelTest(TestCase):

    def setUp(self):
        pass

    def test_obstacle_has_polygons_field(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        # self.assertEqual(obstacle.points.count(), 1)


class AnnotationSerializerTest(TestCase):

    def setUp(self):
        pass

    def test_annotation_serializer_has_obstacles(self):
        annotation = Annotation.objects.create(name='yongjoon')
        Obstacle.objects.create(annotation=annotation)
        Obstacle.objects.create(annotation=annotation)
        serializer = AnnotationSerializer(instance=annotation)
        # self.assertEqual(0, len(serializer.data.get('obstacles')))


class ObstacleSerializerTest(TestCase):

    def setUp(self):
        pass

    def test_annotation_serializer_has_obstacles(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        serializer = AnnotationSerializer(instance=annotation)
        annotation = Annotation.objects.get(name='yongjoon')
        # self.assertEqual(2, len(serializer.data.get('obstacles')))


class PolygonSerializerTest(TestCase):

    def setUp(self):
        pass

    def test_polygon_serializer_test(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        obstacle2 = Obstacle.objects.create(annotation=annotation)

        Point.objects.create(obstacle=obstacle, x=10, y=20)
        Point.objects.create(obstacle=obstacle, x=30, y=40)

        Point.objects.create(obstacle=obstacle2, x=105, y=205)
        Point.objects.create(obstacle=obstacle2, x=305, y=405)

        serializer = AnnotationSerializer(instance=annotation)
        annotation = Annotation.objects.get(name='yongjoon')
        print(json.dumps(serializer.data))
        print(serializer.data.get('obstacles'))
