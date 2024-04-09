from rest_framework.views import APIView
from rest_framework.response import Response
import rest_framework.status as status
from .models import test

class save(APIView):
    def post(self,request):
        try:
            test_instance=test.objects.model(
                name="testing",
                data="testing"
            )
            test_instance.save()
            return Response(data="executed", status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response(data=e,status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
