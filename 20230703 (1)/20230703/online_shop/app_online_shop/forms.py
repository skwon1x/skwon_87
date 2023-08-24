from django import forms

class AdvertisementForm(forms.Form):
    title = forms.CharField(max_length=64,widget=forms.TextInput(attrs={'class':'form-control form-control-lg'}))
    #задаём поле л описания
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-lg'}))
    #задаём поле для цены
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control form-control-lg'}))
    #задаём поле для торга
    auction = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'form-check-input'}),required=False)
    #задаём поле для изображения
    image = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control form-control-lg'}))