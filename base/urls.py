from rest_framework.routers import DefaultRouter

from base.views.about_us import AboutUsView
from base.views.contact_us import ContactUsDetailView, ContactUsFormView
from base.views.dynamic_text import DynamicTextView
from base.views.faq import FAQView
from base.views.footer import FooterView
from base.views.menu import MenuView
from base.views.slider import SliderView
from base.views.state import CityView, StateView
from base.views.terms_and_conditions import TermsAndConditionsView

app_name = "base"

router = DefaultRouter()

router.register(r"faq", FAQView)
router.register(r"about_us", AboutUsView)
router.register(r"contact_us/detail", ContactUsDetailView)
router.register(r"contact_us/form", ContactUsFormView)
router.register(r"menus", MenuView)
router.register(r"sliders", SliderView)
router.register(r"footer", FooterView)
router.register(r"states", StateView)
router.register(r"cities", CityView)
router.register(r"terms-and-conditions", TermsAndConditionsView)
router.register(r"dynamic-texts", DynamicTextView)

urlpatterns = [] + router.urls
