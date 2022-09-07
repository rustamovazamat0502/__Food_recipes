from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("recipy", views.RecipeDataViewSet)

urlpatterns = [
    # path("", views.getData),
    path("", include(router.urls)),
    path("category/", views.category_data, name='categories'),
    path("add_category/", views.add_category_data, name="new_category"),
    path("recipe/", views.recipe_data, name='recipes'),
    path("add_recipe/", views.add_recipe_data, name='new_recipe'),
    path("category_detail/<int:pk>/", views.category_detail, name='category_detail'),
    path("recipe_detail/<int:pk>/", views.recipe_detail, name='recipe_detail'),
    path("category_update/<int:pk>/", views.update_category, name='category_update'),
    path("recipe_update/<int:pk>/", views.update_recipe, name='recipe_update'),
    path("category_delete/<int:pk>/", views.delete_category, name='category_delete'),
    path("recipe_delete/<int:pk>/", views.delete_recipe, name='recipe_delete'),

    path("users_data/", views.users_data, name='users_data'),
]
