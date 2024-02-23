from django import forms
from .models import Restaurant

class RestaurantForm(forms.ModelForm):

    name = forms.CharField(
        label='식당 이름',
        max_length=100
    )
    description = forms.CharField(
        label='식당 설명',
        max_length=250
    )
    address = forms.CharField(
        label='식당 주소',
        widget=forms.Textarea()
    )
    phone_number = forms.CharField(
        label='식당 전화번호',
        widget=forms.Textarea()
    )

    class Meta:
        model = Restaurant
        fields = '__all__'
