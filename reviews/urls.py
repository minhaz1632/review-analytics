from rest_framework import routers

from .views import YelpBusinessItemViewset


review_router = routers.DefaultRouter()
review_router.register(r'yelp-business-items', YelpBusinessItemViewset)
