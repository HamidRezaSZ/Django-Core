from django.urls import re_path

from .consumers import *

websocket_urlpatterns = [
    re_path(r"ws/exam/(?P<id>\d+)/$", ExamConsumer.as_asgi()),
]
