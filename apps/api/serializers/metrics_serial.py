from rest_framework.serializers import ModelSerializer

from apps.api.models.metrics_model import PageStatistics, OfferMetric


class OfferMetricsSerializer(ModelSerializer):
    class Meta:
        model = OfferMetric
        fields = '__all__'


class PageStatisticsSerializer(ModelSerializer):
    class Meta:
        model = PageStatistics
        fields = '__all__'
