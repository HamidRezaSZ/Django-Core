from rest_framework.routers import DefaultRouter
from .views import *

app_name = 'ticketing'

router = DefaultRouter()

router.register(r'ticket', TicketView, basename='ticket')
router.register(r'departments', DepartmentView)
router.register(r'priorities', PriorityView)

urlpatterns = router.urls
