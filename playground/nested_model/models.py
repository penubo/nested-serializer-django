from django.db import models
from django.test.utils import require_jinja2


class Annotation(models.Model):
    name = models.CharField(max_length=60)


class Obstacle(models.Model):
    annotation = models.ForeignKey(Annotation,
                                   related_name='obstacles',
                                   on_delete=models.CASCADE)


class Point(models.Model):
    obstacle = models.ForeignKey(Obstacle,
                                 related_name='polygon',
                                 on_delete=models.CASCADE)

    x = models.FloatField(null=False, blank=False)
    y = models.FloatField(null=False, blank=False)
