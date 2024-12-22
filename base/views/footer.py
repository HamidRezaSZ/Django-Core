from rest_framework.viewsets import ReadOnlyModelViewSet

from base.models import Footer
from base.serializers.footer import FooterSerializer


class FooterView(ReadOnlyModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
