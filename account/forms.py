from django import forms
from django.contrib.auth.models import User
from .models import Account

class AccountForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        model = User
        fields = ('username','email','password')
        labels = {'username':"ユーザーID",'email':"メール"}

class AddAccountForm(forms.ModelForm):
    class Meta():
        model = Account
        fields = ('last_name','first_name','last_kana','first_kana','tel','email','password','account_image')
        labels = {
            'last_name':"名字",
            'first_name':"名",
            'last_kana':"名字(フリガナ)",
            'first_kana':"名(フリガナ)",
            'tel':"電話番号",
            'email':"メールアドレス",
            'password':"パスワード",
            'account_image':"写真"
        }