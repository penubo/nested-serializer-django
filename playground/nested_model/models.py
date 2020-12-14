from django.db import models


class Annotation(models.Model):
    name = models.CharField(max_length=60)


class Obstacle(models.Model):
    annotation = models.ForeignKey(Annotation,
                                   related_name='obstacles',
                                   on_delete=models.CASCADE)


class Point(models.Model):
    obstacle = models.ForeignKey(Obstacle,
                                 related_name='points',
                                 on_delete=models.CASCADE)

    x = models.FloatField(default=0)
    y = models.FloatField(default=0)
