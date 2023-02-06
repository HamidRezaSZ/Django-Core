from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'base'

router = DefaultRouter()

router.register(r'faq', FAQView)
router.register(r'about_us', AboutUsView)
router.register(r'contact_us/detail', ContactUsDetailView)
router.register(r'contact_us/form', ContactUsFormView)
router.register(r'menus', MenuView)
router.register(r'menus', SliderView)
router.register(r'footer', FooterView)
router.register(r'states', StateView)
router.register(r'cities', CityView)
router.register(r'terms-and-conditions', TermsAndConditionsView)

urlpatterns = router.urls