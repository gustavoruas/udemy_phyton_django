from django.db import models
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    
    #auth.User comes from auth class from Django security
    autor = models.ForeignKey("auth.User",on_delete=models.SET_NULL, null=True)
    
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    def get_absolute_url(self):
        return reverse("blog_app:post_detail_url", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return str(self.post_id) + "-" + self.title
    
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    
    post = models.ForeignKey("blog_app.Post",on_delete=models.SET_NULL, null=True, related_name="comments")
    
    author = models.CharField(max_length=400)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    
    approved_comment = models.BooleanField(default=False)
    
    def approve(self):
        self.approved_comment = True
        self.save()
        
    def get_absolute_url(self):
        return reverse("blog_app:post_list_url", kwargs={"pk": self.pk})
    
        
    def __str__(self):
        return str(self.comment_id) + "-" + self.author
    

    
    
    
    
    
    
    