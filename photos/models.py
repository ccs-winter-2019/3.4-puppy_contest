from django.db import models


class Photo(models.Model):
    contest = models.ForeignKey('photos.Contest', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    picture = models.URLField()
    description = models.TextField(null=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Contest(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateField()

    def __str__(self):
        return self.title
