from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Recipe
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, CategoryForm
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .decorators import allowed_users, admin_only
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth.models import User


# Create your views here.


@login_required
def home(request):
    return render(request, "recipe/home.html", {"title": "Home Page"})


# def all_category_recipes(request):
#     recipes = Recipe.objects.all()
#     paginator = Paginator(recipes, 2)
#     number = request.GET.get("page")
#     page_obj = paginator.get_page(number)
#     context = {
#         "recipes": recipes,
#         'page_obj': page_obj
#     }
#
#     return render(request, "recipe/all_recipes.html", context)


class ArticleView(LoginRequiredMixin, ListView):
    model = Recipe
    context_object_name = "recipes"
    template_name = "recipe/all_recipes.html"
    paginate_by = 2
    extra_context = {
        "title": "All Recipes from Classes"
    }


def category_id(request, pk):
    recipes = Recipe.objects.filter(category_id=pk)
    context = {
        "title": f"Category/{pk}/",
        "recipes": recipes,
    }
    return render(request, "recipe/all_recipes.html", context)


@login_required
def recipe_details(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {
        "recipe": recipe,
        "title": recipe.food_name
    }
    return render(request, "recipe/full_recipe.html", context)


@login_required
def add_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = Recipe.objects.create(**form.cleaned_data)
            recipe.save()
            messages.success(request, "Recipe Added Successfully !")
            return redirect("recipe_details", recipe.pk)
    else:
        form = RecipeForm()
    context = {
        "form": form,
        "title": "Add Recipe"
    }
    return render(request, "recipe/recipe_form.html", context)


@login_required
def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            recipe = Category.objects.create(**form.cleaned_data)
            recipe.save()
            messages.success(request, "Category Added Successfully !")
            return redirect("add_recipe")
    else:
        form = CategoryForm()
    context = {
        "form": form,
        "title": "Add Category"
    }
    return render(request, "recipe/categories.html", context)


@login_required
def update_recipe(request, pk):
    # recipe = Recipe.objects.get(id=pk)
    recipe = get_object_or_404(Recipe, id=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.info(request, "Recipe Updated Successfully !")
            return redirect("recipe_details", recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
    context = {
        "form": form,
        "title": recipe.food_name
    }
    return render(request, "recipe/recipe_form.html", context)


@login_required
def delete_recipe(request, pk):
    # recipe = Recipe.objects.get(id=pk)
    recipe = get_object_or_404(Recipe, id=pk)
    if request.method == "POST":
        recipe.delete()
        messages.error(request, "Recipe Deleted Successfully !")
        return redirect("all")
    context = {"recipe": recipe,
               'title': "Delete Recipe"}
    return render(request, 'recipe/delete_recipe.html', context)


# def search_results(request):
#     context = {}
#     if request.method == "GET":
#         word = request.GET.get("q")
#         recipe = Recipe.objects.filter(Q(food_name__icontains=word) | Q(description__icontains=word))
#         total = recipe.count()
#         messages.success(request, f"Total Results: {total}")
#         context.update(
#             {
#                 'recipe': recipe,
#             }
#         )
#     return render(request, 'recipe/all_recipes.html', context)


class SearchView(ArticleView):
    extra_context = {"title": "Search"}

    def get_queryset(self):
        word = self.request.GET.get("q")
        recipe = Recipe.objects.filter(Q(food_name__icontains=word) | Q(description__icontains=word))
        total = recipe.count()
        messages.add_message(self.request, messages.PRIMARY, f"Searched for: {word} ||| Total Results: {total}")
        return recipe


def api_urls(request):
    return render(request, "recipe/api_urls.html")
