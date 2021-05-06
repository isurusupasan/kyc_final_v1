from django import forms
from .models import Kyc_Infotemp, Kyc_Info, Image, Kyc_Reject


class update_forms(forms.ModelForm):
    class Meta:
        model = Kyc_Infotemp
        fields = '__all__'


class accept_form(forms.ModelForm):
    class Meta:
        model = Kyc_Info
        fields = '__all__'

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image
        fields = ('title', 'image')

class reject_forms(forms.ModelForm):
    class Meta:
        model = Kyc_Reject
        fields ='__all__'
        