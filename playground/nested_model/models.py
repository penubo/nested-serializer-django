from django.db import models


class Annotation(models.Model):
    name = models.CharField(max_length=60)


# Create your models here.
class Obstacle(models.Model):
    annotation = models.ForeignKey(Annotation,
                                   related_name='obstacles',
                                   on_delete=models.CASCADE)


class Polygon(models.Model):
    obstacle = models.ForeignKey(Obstacle,
                                 related_name='polygons',
                                 on_delete=models.CASCADE)


class Point(models.Model):
    point = models.ForeignKey(Polygon,
                              related_name='points',
                              on_delete=models.CASCADE)
