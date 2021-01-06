from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    content = models.TextField(max_length = 100000)
    author = models.CharField(max_length = 50)
    last_modified = models.DateTimeField()


    def __str__(self):
        return self.title
