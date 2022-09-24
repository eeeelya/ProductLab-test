from django.urls import path
from handler.views import HandlerView

urlpatterns = [
    path("handler/", HandlerView.as_view()),
]
