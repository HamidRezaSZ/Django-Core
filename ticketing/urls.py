from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'ticketing'

router = DefaultRouter()

router.register(r'tickets', TicketView, basename='ticket')
router.register(r'departments', DepartmentView)
router.register(r'priorities', PriorityView)
router.register(r'status', StatusView)
router.register(r'messages', TicketMessageView)

urlpatterns = router.urls
