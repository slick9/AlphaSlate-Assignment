from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.views import APIView
from PIL import Image

from rest_framework.response import Response

from django.conf import settings

from .serializers import *
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from datetime import datetime
from datetime import timezone
from django.http import HttpResponse
from wsgiref.util import FileWrapper

import os

import uuid

from pprint import pprint

def download(request, file_path):
    try:
        wrapper = FileWrapper(open(file_path, 'rb'))
        response = HttpResponse(wrapper, content_type='application/force-download')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
        return response
    except Exception as e:
        return None


class Base(APIView):
    def get(self,request):
        return render(request,'home.html')

class DownRes(APIView):
    
    def get_resource(self,unique_identifier):
        try:
            model = Resource.objects.get(unique_identifier=unique_identifier)
            return model
        except Resource.DoesNotExist:
            return 
        
    
    def get(self,request,unique_identifier):
        print(unique_identifier)
        if not self.get_resource(unique_identifier):
            return Response(f'Resource with ID = {unique_identifier} Not Found',status = status.HTTP_404_NOT_FOUND)
        serializer = ResSerializer(self.get_resource(unique_identifier))
        file_name = serializer.data['name']

        currentTime = datetime.now().replace(tzinfo=timezone.utc).timestamp()
        linkGenTime = float(serializer.data['time'])
        diff = currentTime - linkGenTime
        print(diff, currentTime, linkGenTime)
        if( diff <= 10800 ):
            rel_path = 'media/'+file_name
            file_path = os.path.join(settings.BASE_DIR, rel_path)
            return download(request, file_path)
        else:
            return render(request,'expired.html',{})

  
class ResList(APIView):

    
    def get(self, request):
        files = []
        for dirname, dirnames, filenames in os.walk('./media'):
            for filename in filenames:
                filename.replace('.', ',')
                files.append(str(filename))
        return render(request,'res_list.html',{'model': files})
        
    def post(self, request):
        unique_identifier = str(uuid.uuid4())
        name = request.POST["name"]
        time = str(datetime.now().replace(tzinfo=timezone.utc).timestamp())
        serializer = ResSerializer(data={'unique_identifier':unique_identifier,'name':name, 'time': time})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return render(request, "goodreq.html", {'uid' : unique_identifier})
        else:
            return render(request,"badreq.html")

 