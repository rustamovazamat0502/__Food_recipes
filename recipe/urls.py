from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("api_urls/", views.api_urls, name="api_urls"),
    # path("paginate/<int:page>", views.page_paginator, name='paginate'),

    # path("all/", views.all_category_recipes, name='all'),
    path("all/", views.ArticleView.as_view(), name='all'),

    path("categories/<int:pk>/", views.category_id, name="categories"),
    path("recipe_details/<int:pk>/", views.recipe_details, name='recipe_details'),

    path("add_recipe/", views.add_recipe, name='add_recipe'),
    path("add_category/", views.add_category, name='add_category'),

    path("update_recipe/<int:pk>/update", views.update_recipe, name='update_recipe'),
    path("delete_recipe/<int:pk>/delete", views.delete_recipe, name='delete_recipe'),

    # path("search_results/", views.search_results, name='search_results')
    path("search_results/", views.SearchView.as_view(), name='search_results')
]
