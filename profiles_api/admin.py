from django.contrib import admin
from profiles_api import models

# Register your models here.
admin.site.register(models.UserProfile)
#we pass the model to Register
admin.site.register(models.ProfileFeedItem)
