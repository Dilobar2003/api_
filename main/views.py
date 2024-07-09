from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CountryModel
from .serializers import CountrySerializer


class CountryAPIView(APIView):
    
    def get(self, request, pk=None):
        if not pk:
           qs = CountryModel.objects.all()
           serializer = CountrySerializer(qs, many=True)
        else:   
            qs = get_object_or_404(CountryModel, pk=pk)
            serializer = CountrySerializer(qs)
        return Response(
            {
                'countries': serializer.data
            }
        )
    
    # def get(self, request, pk):
    #     qs = CountryModel.objects.get(pk=pk)
    #     serializer = CountrySerializer(qs)
    #     return Response(
    #         {
    #             'country': serializer.data
    #         }
    #     )
    
    
    
    def post(self, request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(
                {
                    'status': 'success',
                    'data': serializer.data
                }
            )
        
    def put(self, request, pk):
        country = get_object_or_404(CountryModel, pk=pk)
        serializer = CountrySerializer(instance=country, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        
            return Response(
                {
                    'status': 'success',
                    'data': serializer.data
                }
    
            )
        
    def patch(self, request, pk):
        country = get_object_or_404(CountryModel, pk=pk)
        serializer = CountrySerializer(instance=country, data=request.data)
        if serializer.is_valid():
            serializer.save()
        
            return Response(
                {
                    'status': 'success',
                    'data': serializer.data
                }
            )
            
        
    def delete(self, request, pk):
        object = get_object_or_404(CountryModel, pk=pk)    
        object.delete()
        return Response(
            {
                'status': 'ok'
            }
        )

