from django import forms
from app888 import models


class RegForm(forms.ModelForm):
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = models.UserInfo
        fields = "__all__"
