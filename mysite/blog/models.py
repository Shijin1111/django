from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now(),auto_now=False, auto_now_add=False)
    published_date = models.DateTimeField(blank=True,null=True, auto_now=False, auto_now_add=False)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    
class comments(models.Model):
    post = models.ForeignKey("blog.Post",related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now(),auto_now=False, auto_now_add=False)
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
    def __str__(self):
        return self.text
    