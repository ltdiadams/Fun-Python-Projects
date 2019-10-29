from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import FileSerializer
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class FileView(APIView): # www.website.com/file/upload
    """docstring for FileView."""

    # need to parse the data to post it with post requests
    # formparser for text and whatnot, need multipart for images
    parser_classes = (MultiPartParser, FormParser)

    # say what to do when there is a post request to our django website through our API
    def post(self, request, *args, **kwargs):

        # Creates a serializer with the data we want to POST
        file_serializer = FileSerializer(data=request.data)

        if file_serializer.is_valid():

            # this actually does the HTTP POST request
            file_serializer.save()

            return Response(file_serializer.data, status=status.HTTP_201_CREATED) # 201 means something was created

        else:

            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST) # 201 means something was created


    #def get():, etc...

