from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Product Name', widget=forms.TextInput(
        attrs={"placeholder": "Enter Product"}))

    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Enter Description",
                                          "class": "my_class",
                                          "id": "my_id",
                                          "rows": 10,
                                          "cols": 50
                                      }
                                  )
                                  )
    price = forms.DecimalField(initial=99.99)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]
    #Validation for Title
    def clean_title(self, *args, **kargs):
        title=self.cleaned_data.get("title")
        # if not title.startswith("Product"):
        #     raise forms.ValidationError("Enter Valid Product")
        return title


class RawProductForm(forms.Form):
    title = forms.CharField(label='Product Name', widget=forms.TextInput(
        attrs={"placeholder": "Enter Product"}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "placeholder": "Enter Description",
                                          "class": "my_class",
                                          "id": "my_id",
                                          "rows": 10,
                                          "cols": 50
                                      }
                                  )
                                  )
    price = forms.DecimalField(initial=99.99)
