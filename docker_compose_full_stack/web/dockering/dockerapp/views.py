from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView

from .models import Foo
from .serializers import FooSerializer


def index(request):
    return HttpResponse("Hello, world!")


class FoosView(ListCreateAPIView):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer
