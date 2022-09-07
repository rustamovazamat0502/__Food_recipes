from PIL import Image
from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse("categories", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Recipe(models.Model):
    food_name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    ingredients = models.TextField(blank=False)
    method = models.TextField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    video = models.FileField(upload_to="videos/", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # def save(self, **kwargs):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (200, 200)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def get_absolute_url(self):
        return reverse("recipe_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.food_name

    def __repr__(self):
        return f'Recipe(pk={self.pk}, title="{self.food_name}")'

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['-created_at']
