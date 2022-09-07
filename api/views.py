from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipe.models import Recipe, Category
from django.contrib.auth.models import User
from .serializers import CategorySerializer, RecipeSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework import permissions


class RecipeDataViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all().order_by("-created_at")
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def category_data(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_detail(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def add_category_data(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def add_recipe_data(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def recipe_data(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def recipe_detail(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(recipe, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def update_category(request, pk):
    category = Category.objects.get(id=pk)
    serializer = CategorySerializer(instance=category, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["GET", 'POST'])
def update_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def delete_category(request, pk):
    category = Category.objects.get(id=pk)
    category.delete()
    return Response("Category deleted successfully !!!")


@api_view(['DELETE'])
def delete_recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return Response("Recipe deleted successfully !!!")


@api_view(['GET'])
def users_data(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
