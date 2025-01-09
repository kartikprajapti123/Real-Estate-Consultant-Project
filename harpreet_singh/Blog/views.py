from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action

from Blog.models import Blog
from Blog.serializer import BlogSerializer
from rest_framework.pagination import PageNumberPagination


class mypagination(PageNumberPagination):
    page_size = 10

class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = mypagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "title",
        "description",
        "created_at"
    ]
    ordering_fields = [
        "title",
        "created_at"
    ]

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"success": True, "data": serializer.data},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"success": False, "message": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        no_pagination = request.query_params.get("no_pagination")
        if no_pagination:
            serializer = self.serializer_class(queryset, many=True)
            return Response({"success": True, "data": serializer.data})

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            return self.get_paginated_response(
                {"success": True, "data": serializer.data}
            )

        serializer = self.serializer_class(queryset, many=True)
        return self.get_paginated_response({"success": True, "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()  # Perform a hard delete. Use soft delete if needed.
        return Response(
            {"success": True, "message": "Blog deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )

    @action(detail=False, methods=['GET'], url_path='blog_by_title')
    def blog_by_title(self, request, *args, **kwargs):
        title = request.query_params.get("title")
        
        if title:
            try:
                blog_instance = Blog.objects.get(title=title)
            except Blog.DoesNotExist:
                return Response(
                    {"success": False, "message": "No blog found with this title"},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            return Response(
                {"success": False, "message": "Title is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        serializer = BlogSerializer(blog_instance)
        return Response(
            {"success": True, "data": serializer.data},
            status=status.HTTP_200_OK
        )
