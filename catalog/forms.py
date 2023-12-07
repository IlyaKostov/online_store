from django import forms

from catalog.models import Product, Version


class FormClassMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(FormClassMixin, forms.ModelForm):
    bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'user')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        self.check_bad_words(self.bad_words, cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        self.check_bad_words(self.bad_words, cleaned_data)
        return cleaned_data

    @staticmethod
    def check_bad_words(bad_words, cleaned_data):
        for word in bad_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Слово {word} запрещено использовать')


class ManagerProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published')


class VersionForm(FormClassMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
