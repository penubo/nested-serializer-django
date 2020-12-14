from .serializers import AnnotationSerializer
from .models import Annotation, Obstacle, Polygon
from django.test import TestCase

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
        Polygon.objects.create(obstacle=obstacle)
        self.assertEqual(obstacle.polygons.count(), 1)


class AnnotationSerializerTest(TestCase):

    def setUp(self):
        pass

    def test_annotation_serializer_has_obstacles(self):
        annotation = Annotation.objects.create(name='yongjoon')
        Obstacle.objects.create(annotation=annotation)
        Obstacle.objects.create(annotation=annotation)
        serializer = AnnotationSerializer(instance=annotation)
        self.assertEqual(2, len(serializer.data.get('obstacles')))


class ObstacleSerializerTest(TestCase):

    def setUp(self):
        pass

    def test_annotation_serializer_has_obstacles(self):
        annotation = Annotation.objects.create(name='yongjoon')
        obstacle = Obstacle.objects.create(annotation=annotation)
        Polygon.objects.create(obstacle=obstacle)
        serializer = AnnotationSerializer(instance=annotation)
        print(serializer.data)
        # self.assertEqual(2, len(serializer.data.get('obstacles')))
