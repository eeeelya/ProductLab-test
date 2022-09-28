import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from handler.parser import run_tasks
from handler.schemas import ArticleListModel, ArticleModel
from handler.serializers import InputSerializer
from handler.utils import make_article_list

logger = logging.getLogger(__name__)


class HandlerView(APIView):
    def post(self, request):
        article_serializer = InputSerializer(data=request.data)
        article_serializer.is_valid(raise_exception=True)

        if "article_file" in article_serializer.data:
            articles = make_article_list(request.FILES.get("article_file"))

            if not articles:
                return Response({"detail": "Articles not found."}, status=status.HTTP_404_NOT_FOUND)

            result = run_tasks(articles)

            ArticleListModel(items=result)

            return Response(result, status=status.HTTP_200_OK)

        if "single_article" in article_serializer.data:
            result = run_tasks([article_serializer.data["single_article"]])

            ArticleModel(**result[0])

            return Response(result[0], status=status.HTTP_200_OK)

        return Response(status=status.HTTP_400_BAD_REQUEST)
