from django.contrib import admin
from reviews.models import Review, YelpBusinessItem

# Register your models here.
admin.site.register(Review)
admin.site.register(YelpBusinessItem)
