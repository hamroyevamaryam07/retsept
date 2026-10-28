
from django.shortcuts import render, get_object_or_404
from .models import Recipe


def home(request):
    retseptlar = Recipe.objects.all()

    return render(
        request,
        "retseptapp/home.html",
        {"retseptlar": retseptlar}
    )


def recipe_detail(request, pk):
    retsept = get_object_or_404(Recipe, pk=pk)

    return render(
        request,
        "retseptapp/recipe_datali.html",
        {"retsept": retsept}
    )
