from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Pdf_management.models import PdfManagement
from Pdf_management.serializer import PdfManagementSerializer
from rest_framework.response import Response
from rest_framework import status

class PdfManagementViewset(viewsets.ModelViewSet):
    
    queryset=PdfManagement.objects.all()
    
    serializer_class=PdfManagementSerializer
    
    def list(self, request, *args, **kwargs):
        
        queryset=self.filter_queryset(self.get_queryset())
        
        no_pagination=request.query_params.get("no_pagination")
        if no_pagination:
            serializer=self.serializer_class(queryset,many=True)
            return Response({"success":"True","data":serializer.data},status=status.HTTP_200_OK)
        
        page=self.paginate_queryset(queryset)
        if page is not None:
            serializer=self.serializer_class(page,many=True)
            return self.get_paginated_response({"success":"True","data":serializer.data},status=status.HTTP_200_OK)
 
        serializer=self.serializer_class(queryset,many=True)
        return Response({"success":"True","data":serializer.data},status=status.HTTP_200_OK)
        
        
        
        
    def create(self, request, *args, **kwargs):
        data=request.data
        serializer=self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"True","message":"File Saved Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"success":"False","message":"Error occoured"},status=status.HTTP_400_BAD_REQUEST)
        
        
    def update(self, request, *args, **kwargs):
        id=self.get_object()
        data=request.data
        serializer=self.serializer_class(id=id,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":"True","message":"File Updated Successfully"},status=status.HTTP_200_OK)
        else:
            return Response({"success":"False","message":"Error occoured"},status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def retrieve(self, request, *args, **kwargs):
        instance=self.get_object()
        serializer=self.serializer_class(instance)
        return Response({"success":"True","data":serializer.data},status=status.HTTP_200_OK)
        
        
    def destroy(self,request,*args, **kwargs):
        instance=self.get_object()
        instance.delete()
        return Response({"success":"True","message":"File Deleted Successfully"},status=status.HTTP_200_OK)
        

    
        
        