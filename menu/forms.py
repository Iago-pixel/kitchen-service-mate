from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

from menu.models import Cook, Dish, Ingredient


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "years_of_experience", "email")


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

    class Meta:
        model = Dish
        fields = "__all__"
