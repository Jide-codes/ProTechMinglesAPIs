from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    kudos = models.ManyToManyField(User, related_name='post_kudos', blank=True)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return f"{self.body[:20]}... ({self.created.strftime('%Y-%m-%d %H:%M:%S')})"
        
    def total_kudos(self):
        return self.kudos.count()
    
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"{self.body[:20]}... ({self.created.strftime('%Y-%m-%d %H:%M:%S')})"
        
        
    # def total_comments(self):
    #     return self.post.comments.count()
    
    
class UserFollow(models.Model):
    user = models.OneToOneField(User, related_name='current_user', on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name='current_user_followers', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def total_currentUser_following(self):
        return self.following.count()
    
    def total_currentUser_followers(self):
        return self.user.current_user_followers.count()
    
    def currentUser_followers_list(self):
        followers_list = []
        for users in self.user.current_user_followers.all():
            followers_list.append(users.id)
        return followers_list