from django.db import models
from django.contrib.auth.models import User

class Community(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
    members = models.ManyToManyField(User, related_name="communities")
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Communitie"
    
    def __str__(self):
        return f"{self.name} community | created by -- {self.creator}"

# class Member(models.Model):
#     community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="members_community")
#     community_member = models.ForeignKey(User, on_delete=models.CASCADE, related_name="community_user")
#     joined_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.community_member} joined {self.community}"


class CommunityPost(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name="community_post")
    author= models.ForeignKey(User,on_delete=models.CASCADE, related_name="post_author")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    kudos = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    def __str__(self):
        return f"{self.body[:20]} | {self.author} | {self.community}"
    
    
    def kudos_count(self):
        return self.kudos.count()
    

class CommunityComment(models.Model):
    post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="comment_author")
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.content[:20]} | {self.author}| {self.post}|"
    
    def total_comments(self):
        return self.post.comments.count()