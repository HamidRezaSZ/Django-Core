from rest_framework.viewsets import ModelViewSet as BaseModelViewSet


class ModelViewSet(BaseModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except Exception:
            return [permission() for permission in self.permission_classes]
