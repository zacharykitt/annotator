from django.db import models


# Create your models here.
class Comment(models.Model):
    code = models.CharField(max_length=10)
    text = models.TextField()
    reviewed_by = models.SmallIntegerField(default=0)
    in_review_by = models.SmallIntegerField(default=0)


class Tag(models.Model):
    text = models.CharField(max_length=32)
    color = models.CharField(default='light', max_length=12)
    comments = models.ManyToManyField(Comment)

    def __unicode__(self):
        return self.text
