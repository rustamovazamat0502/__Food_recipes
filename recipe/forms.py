from django import forms
from .models import Recipe, Category


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'food_name',
            'description',
            'ingredients',
            'method',
            'image',
            "video",
            'category'
        ]

        widgets = {
            "food_name": forms.TextInput(attrs={
                "placeholder": 'food name'
            }),
            "description": forms.TextInput(attrs={
                "placeholder": 'description'
            }),
            "ingredients": forms.Textarea(attrs={
                "placeholder": 'ingredients'
            }),
            "method": forms.Textarea(attrs={
                "placeholder": 'method'
            }),
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']

        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": 'Title'
            })
        }
