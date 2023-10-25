from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializers, ProductSerializers
from .models import Category, Product


# class CategoryView(APIView):
#     def get(self, request):
#         queryset = Category.objects.all()
#         serializer = CategorySerializers(instance=queryset, many=True)
#         return Response(serializer.data, status=200)
#
#     def post(self, request):
#         serializer = CategorySerializers(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=201)
#
#
# class CategoryDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             category = Category.objects.get(slug=pk)
#             return category
#         except Category.DoesNotExist:
#             raise Http404('Not found')
#
#     def put(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializers(instance=category ,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=200)
#
#     def get(self, request, pk):
#         category = self.get_object(pk)
#         serializer = CategorySerializers(instance=category)
#         return Response(serializer.data, status=200)
#
#     def delete(self, request, pk):
#         category = self.get_object(pk)
#         category.delete()
#         return Response('Successfully deleted', status=204)
#
#
# class ProductView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers
#
#
# class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializers


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers