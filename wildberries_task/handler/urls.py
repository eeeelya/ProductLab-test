from django.urls import path
from handler.views import HandlerFileView, HandlerArticleView

urlpatterns = [
    path("handle-file/", HandlerFileView.as_view()),
    path("handle-article/", HandlerArticleView.as_view())
]
