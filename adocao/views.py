from rest_framework.views import APIView
from .serializer import AdocaoSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST

class AdocaoList(APIView):
    def post(self, request, format=None):
        serializer = AdocaoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(
            {
                "errors": serializer.errors,
                "message":"Houveram erros de validação"
            }, 
            status= HTTP_400_BAD_REQUEST
            )