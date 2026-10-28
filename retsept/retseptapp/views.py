from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from .models import Recipe
from .forms import RecipeForm

# Barcha foydalanuvchilar ko‘radigan bosh sahifa (Qidiruv tizimi bilan)
def home(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        # Taom nomi yoki masalliqlar matni ichidan qidiradi
        natijalar = Recipe.objects.filter(
            Q(nom__icontains=query) | Q(masalliqlar__icontains=query)
        )
        
        # AGAR AYNAN BITTA TAOM TOPILSA -> TO‘G‘RIDAN-TO‘G‘RI O‘SHA TAOM SAHIFASIGA O‘TADI
        if natijalar.count() == 1:
            return redirect('recipe_detail', pk=natijalar.first().pk)
        
        # Agar birdan ko‘p taom topilsa, o‘shalarni ro‘yxat qilib bosh sahifada ko‘rsatadi
        retseptlar = natijalar
    else:
        # Qidiruv bo‘lmasa, barcha retseptlarni ko‘rsatadi
        retseptlar = Recipe.objects.all()

    return render(
        request, 
        "retseptapp/home.html", 
        {"retseptlar": retseptlar, "query": query}
    )

# Retseptning batafsil sahifasi
def recipe_detail(request, pk):
    retsept = get_object_or_404(Recipe, pk=pk)
    return render(request, "retseptapp/recipe_datali.html", {"retsept": retsept})

# FAQAT ADMIN KIRA OLADIGAN SHAXSIY DASHBOARD
@user_passes_test(lambda u: u.is_superuser)
def custom_admin_dashboard(request):
    retseptlar = Recipe.objects.all()
    return render(request, 'retseptapp/admin_dashboard.html', {'retseptlar': retseptlar})

# Yangi retsept qo‘shish
@user_passes_test(lambda u: u.is_superuser)
def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Yangi retsept muvaffaqiyatli qo‘shildi!")
            return redirect('custom_admin_dashboard')
    else:
        form = RecipeForm()
    return render(request, 'retseptapp/recipe_form.html', {'form': form, 'title': "Yangi retsept qo‘shish"})

# Retseptni tahrirlash
@user_passes_test(lambda u: u.is_superuser)
def recipe_update(request, pk):
    retsept = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=retsept)
        if form.is_valid():
            form.save()
            messages.success(request, "Retsept muvaffaqiyatli yangilandi!")
            return redirect('custom_admin_dashboard')
    else:
        form = RecipeForm(instance=retsept)
    return render(request, 'retseptapp/recipe_form.html', {'form': form, 'title': "Retseptni tahrirlash"})

# Retseptni o‘chirish
@user_passes_test(lambda u: u.is_superuser)
def recipe_delete(request, pk):
    retsept = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        retsept.delete()
        messages.success(request, "Retsept o‘chirib tashlandi!")
        return redirect('custom_admin_dashboard')
    return render(request, 'retseptapp/recipe_confirm_delete.html', {'retsept': retsept})
