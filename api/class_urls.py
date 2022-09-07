from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import class_views

urlpatterns = [
    path("category/", class_views.CategoryList.as_view(), name='categories'),
    path("category_detail/<int:pk>/", class_views.CategoryDetail.as_view(), name='category_detail'),
    path("category_create/", class_views.CategoryCreate.as_view(), name='category_create'),
    path("category_update/<int:pk>/", class_views.CategoryUpdate.as_view(), name='category_update'),
    path("category_delete/<int:pk>/", class_views.CategoryDelete.as_view(), name='category_delete'),

    path("recipe/", class_views.RecipeList.as_view(), name='recipes'),
    path("recipe_detail/<int:pk>/", class_views.RecipeDetail.as_view(), name='recipe_detail'),
    path("recipe_create/", class_views.RecipeCreate.as_view(), name='recipe_create'),
    path("recipe_update/<int:pk>/", class_views.RecipeUpdate.as_view(), name='recipe_update'),
    path("recipe_delete/<int:pk>/", class_views.RecipeDelete.as_view(), name='recipe_delete'),

    path("users_data/", class_views.UsersList.as_view(), name='users_data'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
