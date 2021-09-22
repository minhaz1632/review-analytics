from rest_framework import serializers
from rest_framework.exceptions import PermissionDenied, ValidationError
from urllib.parse import urlparse

from .models import YelpBusinessItem
from user_profile.serializers import UserInfoSerializer


YELP_BASE_URL = 'yelp.com'


def parse_business_page_url(url):
    parsed_url = urlparse(url)
    subpaths = parsed_url.path.strip('/').split('/')

    if len(subpaths) < 2 or YELP_BASE_URL not in parsed_url.netloc:
        raise ValidationError('Please provide a valid Yelp url')

    business_page_url = f'{parsed_url.scheme}://{parsed_url.netloc}/{subpaths[0]}/{subpaths[1]}'

    return business_page_url


class YelpBusinessItemSerializer(serializers.ModelSerializer):
    created_by = UserInfoSerializer(read_only=True)

    class Meta:
        model = YelpBusinessItem
        fields = '__all__'
        read_only_fields = ['date_created']

    def create(self, validated_data):
        request = self.context.get("request")
        url = validated_data.pop('url')
        business_page_url = parse_business_page_url(url)

        if request and hasattr(request, "user"):
            user = request.user
        else:
            raise PermissionDenied('User not authenticated!', code=403)

        obj = YelpBusinessItem.objects.create(**validated_data, url=business_page_url, created_by=user)
        return obj

    def update(self, instance, validated_data):
        url = validated_data.pop('url')
        business_page_url = parse_business_page_url(url)

        for dict_key in validated_data:
            setattr(instance, dict_key, validated_data[dict_key])

        setattr(instance, 'url', business_page_url)
        return instance

