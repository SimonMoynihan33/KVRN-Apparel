from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """
    Form for creating and updating Product instances.

    Includes fields for selecting multiple categories (with help text for
    graphic collection guidelines) and allows the upload of primary and
    secondary images with custom widgets.
    """

    class Meta:
        model = Product
        fields = '__all__'

    # Customize the category field help text
    categories = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        help_text="Please only select multiple categories when it relates to \
            the Graphic Collection (e.g. Graphic Tshirt = Graphic T-Shirt\
                + T-Shirt)"
    )

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    image2 = forms.ImageField(
        label='Secondary Image', required=False,
        widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        """
        Initialize the form with a friendly name display for categories and
        apply custom styling to all form fields.
        """
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['categories'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
