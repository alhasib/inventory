from django import forms
from django.contrib.auth.models import User,Permission
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple

class NameChoiceField(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return f'{obj.name}'


class UserForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group form_field col-md-5 bg-light'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-group form_field col-md-5 bg-light', 'placeholder':"Enter Password..."}))
    permission = NameChoiceField(queryset=Permission.objects.all(), widget=forms.CheckboxSelectMultiple)



    # class Meta:
    #     # model = User 
    #     fields = ['username', 'password','permission']

    #     help_texts = {
    #         'email':None,
    #         'username':None,
    #     }

    #     widgets = {
    #         'username':forms.TextInput(attrs={'class':'form-group form_field col-md-5 bg-light', 'placeholder':"Enter Username..."}),
    #         'email':forms.TextInput(attrs={'class':'form-control form_field bg-light', 'placeholder':"Enter Email..."})

    #     }



    # def save(self):
    #     password = self.cleaned_data.pop('password')
    #     user = super().save()
    #     user.set_password(password)
    #     user.save()
    #     return user 



class AddPermissionForm(forms.Form):
    user = forms.ModelChoiceField(widget = forms.Select(attrs={'class':'form-group col-lg-3 form_field',}), queryset=Permission.objects.all())
    permission = forms.ModelMultipleChoiceField(queryset=Permission.objects.values_list('name', flat = True), widget=forms.CheckboxSelectMultiple)
