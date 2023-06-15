"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Core API",
        default_version='v1',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    url='',
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = i18n_patterns(
    # apps
    path('api/blog/', include('blog.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/base/', include('base.urls')),
    path('api/products/', include('products.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/exams/', include('exams.urls')),
    path('api/newsletters/', include('newsletters.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/ticketing/', include('ticketing.urls')),
    path('api/courses/', include('courses.urls')),


    # rosetta (multiple language package)
    re_path(r'^rosetta/', include('rosetta.urls')),

    # ckeditor (Text Editor)
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # Text editor

    # swgger
    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger',
            cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc',
            cache_timeout=0), name='schema-redoc'),

    # admin panel
    path('', admin.site.urls),
)
