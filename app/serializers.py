from rest_framework import serializers
from .models import Enquiry,NewsLetter


class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        depth=3
        exclude = ['id']
        field = "__all__"
class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsLetter
        depth=3
        exclude = ['id']
        field = "__all__"