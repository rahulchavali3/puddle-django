from django import forms

from .models import Item


INPUT_CLASSES = (
    'w-full py-4 px-6 rounded-xl border border-gray-200 '
    'bg-gray-50 text-gray-800 '
    'focus:outline-none focus:ring-2 focus:ring-teal-500 '
    'focus:border-transparent transition'
)


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES,
            }),

            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item name',
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Describe your item...',
                'rows': 5,
            }),

            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter price',
                'min': '0',
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter item name',
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Describe your item...',
                'rows': 5,
            }),

            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES,
                'placeholder': 'Enter price',
                'min': '0',
            }),

            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES,
            }),

            'is_sold': forms.CheckboxInput(attrs={
                'class': 'w-5 h-5 text-teal-600 rounded '
                         'focus:ring-teal-500',
            }),
        }