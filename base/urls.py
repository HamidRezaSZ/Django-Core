from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import *

app_name = 'base'

router = DefaultRouter()

router.register(r'faq', FAQView)
router.register(r'about_us', AboutUsView)
router.register(r'contact_us/detail', ContactUsDetailView)
router.register(r'contact_us/form', ContactUsFormView)
router.register(r'menus', MenuView)
router.register(r'sliders', SliderView)
router.register(r'footer', FooterView)
router.register(r'states', StateView)
router.register(r'cities', CityView)
router.register(r'terms-and-conditions', TermsAndConditionsView)
router.register(r'dynamic-texts', DynamicTextView)

urlpatterns = router.urls
