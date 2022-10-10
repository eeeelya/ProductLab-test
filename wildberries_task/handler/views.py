import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from handler.parser import run_tasks, run_single_task
from handler.serializers import InputFileSerializer, InputArticleSerializer
from handler.utils import make_article_list

logger = logging.getLogger(__name__)


class HandlerFileView(APIView):
    def post(self, request):
        file_serializer = InputFileSerializer(data=request.FILES)
        file_serializer.is_valid(raise_exception=True)

        articles = make_article_list(request.FILES.get("article_file"))

        if not articles:
            return Response({"detail": "Articles in file not found"}, status=status.HTTP_404_NOT_FOUND)

        result = run_tasks(articles)

        return Response(result, status=status.HTTP_200_OK)


class HandlerArticleView(APIView):
    def post(self, request):
        article_serializer = InputArticleSerializer(data=request.data)
        article_serializer.is_valid(raise_exception=True)

        article = article_serializer.data["article"]

        result = run_single_task(article)

        if not result:
            return Response({"detail": f"Article {article} not found"}, status=status.HTTP_404_NOT_FOUND)

        return Response(result, status=status.HTTP_200_OK)
