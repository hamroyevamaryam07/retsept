from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['nom', 'tavsif', 'tur', 'vaqt', 'rasm', 'masalliqlar', 'tayyorlash_usuli']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Taom nomi'}),
            'tavsif': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Qisqacha tavsif...'}),
            'tur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: Suyuq taom, Somsa'}),
            'vaqt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: 40 daqiqa'}),
            'rasm': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Rasm URL manzili'}),  # BU YER TO‘G‘RILANDI
            'masalliqlar': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Har birini yangi qatordan yozing'}),
            'tayyorlash_usuli': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Tayyorlash bosqichlari...'}),
        }
