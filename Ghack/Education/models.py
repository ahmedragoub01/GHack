from django.db import models


class Videos (models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    rating = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Books (models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    rating = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Courses (models.Model):
    course_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    rating = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Podcasts (models.Model):
    podcast_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.CharField(max_length=100)
    rating = models.IntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title