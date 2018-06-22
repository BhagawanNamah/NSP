from django.contrib import admin
from .models import ProjectDetail, UserProfile
from accounts.models import User, Follow, ProjectPeopleInterested

admin.site.site_title = "NSP"
admin.site.index_title = "NSP"
admin.site.site_header = "NSP ADMINISTRATION"

admin.site.register(User)
admin.site.register(ProjectDetail)
admin.site.register(UserProfile)
admin.site.register(Follow)
admin.site.register(ProjectPeopleInterested)