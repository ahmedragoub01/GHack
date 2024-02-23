from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    upvotes = models.ManyToManyField(User, related_name='upvoted_posts')
    downvotes = models.ManyToManyField(User, related_name='downvoted_posts')
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    Comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name ="comments", on_delete=models.CASCADE)
    body = models.TextField()
    upvotes = models.ManyToManyField(User, related_name='upvoted_comments')
    downvotes = models.ManyToManyField(User, related_name='downvoted_comments')
    rating = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.user.username)





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    financial_goals = models.TextField(blank=True)
    # more info

    def __str__(self):
        return self.user.username

class FinancialCounselor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=100)
    availability = models.CharField(max_length=50)
    bio = models.TextField(blank=True)
    # more info

    def __str__(self):
        return self.user.username

class Consultation(models.Model):
    user = models.ForeignKey(User, related_name='user_consultations', on_delete=models.CASCADE)
    counselor = models.ForeignKey(FinancialCounselor, related_name='counselor_consultations', on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Consultation between {self.user.username} and {self.counselor.user.username}"

class Message(models.Model):
    consultation = models.ForeignKey(Consultation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in {self.consultation}"

class Goal(models.Model):
    user = models.ForeignKey(User, related_name='goals', on_delete=models.CASCADE)
    goal = models.TextField()
    date_set = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Goal for {self.user.username}"
    

