from django.urls import path
from .views import FileView

urlpatterns = [
    path('upload/', FileView.as_view(), name='file-upload') # renders our data in django, as_view() in APIView
    # django needs to render our data before it sends it over as an HTTP POST request
]
