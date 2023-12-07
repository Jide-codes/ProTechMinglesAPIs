from django.contrib import admin
from .models import Community, CommunityPost, CommunityComment

admin.site.register(Community)
admin.site.register(CommunityPost)
admin.site.register(CommunityComment)
