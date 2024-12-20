from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    """
    Form for capturing order details.

    Uses the Order model fields to collect essential information from
    the user for processing an order, including contact information
    and address details.
    """

    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "postcode",
            "country",
            "county",
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County/State",
        }

        self.fields["full_name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "country":
                placeholder = (
                    f"{placeholders[field]} *"
                    if self.fields[field].required
                    else placeholders[field]
                )
                self.fields[field].widget.attrs["placeholder"] = placeholder
            # Add common CSS class to all fields
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False

        self.fields["country"].choices = [("", "Select Country")] + list(
            self.fields["country"].choices
        )
