from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser


from forex_backends.common import rest_utils
from editorial.models import ArticleActivity
from .serializers import ArticleActivitySerializer


class ArticleActivityView(generics.GenericAPIView):
    serializer_class = ArticleActivitySerializer
    parser_classes = (MultiPartParser,FormParser,JSONParser,)

    def get(self, request, format=None):
        try:
            article_activity_obj = ArticleActivity.objects.all()
            serializer = self.serializer_class(article_activity_obj,many=True)
            message = "Ok"
            return rest_utils.build_response(
                status.HTTP_200_OK, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

    def post(self, request, format=None):
        try:
            serializer = ArticleActivitySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                message = "Created"
                return rest_utils.build_response(
                    status.HTTP_201_CREATED, message, data=serializer.data, errors=None
                )
            else:
                return rest_utils.build_response(
                    status.HTTP_400_BAD_REQUEST,
                    rest_utils.HTTP_REST_MESSAGES["400"],
                    data=None,
                    errors=serializer.errors,
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )
            
class SingleArticleActivityView(generics.GenericAPIView):
    serializer_class = ArticleActivitySerializer
    parser_classes = (MultiPartParser,FormParser,)
    # permission_classes = [IsAuthenticated]

    def get(self, request,id, format=None):
        try:
            article_activity = ArticleActivity.objects.filter( id=id)
            serializer = self.serializer_class(article_activity, many=True)
            message = "Ok"
            return rest_utils.build_response(
                status.HTTP_200_OK, message, data=serializer.data, errors=None
            )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

    
    def put(self, request, id, format=None):
        try:
            article_activity = ArticleActivity.objects.get(id=id)
            serializer = self.serializer_class(article_activity, data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = "ArticleActivity Successfully Updated"
                return rest_utils.build_response(
                    status.HTTP_200_OK, message, data=serializer.data, errors=None
                )
            else:
                return rest_utils.build_response(
                    status.HTTP_400_BAD_REQUEST,
                    rest_utils.HTTP_REST_MESSAGES["400"],
                    data=None,
                    errors=serializer.errors,
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )


    def patch(self, request, id, format=None):
        try:
            articleactivity = ArticleActivity.objects.get(id=id)
            serializer = self.serializer_class(
                articleactivity, data=request.data, partial=True
            )  # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
                message = "Article Activity Successfully Updated"
                return rest_utils.build_response(
                    status.HTTP_200_OK, message, data=serializer.data, errors=None
                )
            else:
                return rest_utils.build_response(
                    status.HTTP_400_BAD_REQUEST,
                    rest_utils.HTTP_REST_MESSAGES["400"],
                    data=None,
                    errors=serializer.errors,
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )

    def delete(self, request, id, format=None):
        try:
            articleactivity = ArticleActivity.objects.filter(id=id)
            if articleactivity.exists():
                articleactivity.delete()
                message = "Article Successfully Deleted"
                return rest_utils.build_response(
                        status.HTTP_204_NO_CONTENT, message, data=None, errors=None
                )
            else:
                return rest_utils.build_response(
                    status.HTTP_404_NOT_FOUND,
                    rest_utils.HTTP_REST_MESSAGES["404"],
                    data=None,
                    errors=None,
                )
        except Exception as e:
            message = rest_utils.HTTP_REST_MESSAGES["500"]
            return rest_utils.build_response(
                status.HTTP_500_INTERNAL_SERVER_ERROR, message, data=None, errors=str(e)
            )        
