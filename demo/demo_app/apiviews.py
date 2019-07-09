from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.renderers import TemplateHTMLRenderer
import json
from datetime import datetime

from django.shortcuts import get_object_or_404

from .models import biomodel
from .serializers import BioModelSerializer

class BioModelList(APIView):
    # queryset = biomodel.objects.all()
    # serializer_class = BioModelSerializer
    def get(self, request):
        bio_objects = biomodel.objects.all()
        data = BioModelSerializer(bio_objects, many=True).data
        return Response(data)

class BioModelDetails(APIView):
    def get(self, request, key):
        bio_objects = get_object_or_404(biomodel, bmKey=key)
        data = BioModelSerializer(bio_objects).data
        return Response(data)
    # def post():
    #     pass

class BioModelSearch(APIView):
    renderer_classes = (TemplateHTMLRenderer, )
    def get(self, request):
        bmName = request.query_params.get('bmName').replace("+", " ")
        bmId = request.query_params.get('bmId')
        category = request.query_params.get('category')
        owner = request.query_params.get('owner')
        savedLow = request.query_params.get('savedLow')
        savedHigh = request.query_params.get('savedHigh')
        sartRow = request.query_params.get('startRow')
        maxRows = request.query_params.get('maxRows')
        orderby = request.query_params.get('orderBy')

        if bmId == "all" and bmName == "all" and owner == "all":
            bio_objects = biomodel.objects.all()[int(sartRow):int(maxRows)]
        else:
            if orderby == 'name_desc':
                orderby = '-name'
            elif orderby == 'name_asc':
                orderby = 'name'

            if category == 'all' or category == 'public':
                bio_objects = biomodel.objects.filter(bmKey=bmId, name=bmName, ownerName=owner).order_by(orderby)
                print("BioOBJECTS",bio_objects)
            else:
                bio_objects =  biomodel.objects.filter(biomodel, bmKey=bmId, name=bmName, ownerName=category).order_by(orderby)
        data = BioModelSerializer(bio_objects, many=True).data
        data = json.dumps(data)
        data = json.loads(data)
        print(len(data))
        for x in data:
            x ['formatDate'] = x['saveDate'][:10]
            x['formatDate'] = datetime.strptime(x['formatDate'], "%Y-%m-%d" )
            x['formatDate'] = x['formatDate'].strftime("%b %d, %Y")
        return Response({'data': data, 'len':len(data)},  template_name = 'index.html')