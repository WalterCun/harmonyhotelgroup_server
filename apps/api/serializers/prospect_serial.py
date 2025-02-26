from rest_framework.serializers import ModelSerializer

from apps.api.models.prospect_model import Prospect, ProspectSource, ProspectSubject


class ProspectSubjectSerializer(ModelSerializer):
    class Meta:
        model = ProspectSubject
        fields = '__all__'


class ProspectSourceSerializer(ModelSerializer):
    class Meta:
        model = ProspectSource
        fields = '__all__'


class ProspectSerializer(ModelSerializer):
    subject = ProspectSubjectSerializer
    source = ProspectSourceSerializer
    class Meta:
        model = Prospect
        fields = '__all__'
