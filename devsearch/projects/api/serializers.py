from rest_framework.serializers import ModelSerializer
from ..models import Project

class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description',
                  'demo_link', 'source_link', 'created')
