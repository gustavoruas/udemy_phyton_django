from django.db import models
from django.urls import reverse
from django.conf import settings
from groups.models import Group
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.SET_NULL, null=True)
    
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts",on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.message
    
    def save(self, *args, **kwargs):
        self.message_html = self.message
        super().save(*args, **kwargs)
        
    def get_absolute_url(self):
        return reverse("posts:post_single_url", kwargs={"pk": self.pk
                                               ,"username":self.user.username
                                               })
    
    class Meta:
        ordering = ["-created_at"]
        unique_together = ["user","message"]
    #pass # this concludes the class without any code




