#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django import forms
from .models import Subscriber,Administrator

class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(widget = forms.PasswordInput())
   
    class Meta:
        model =User
        fields=['username','password']

class SignUpForm(forms.ModelForm):
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    username = forms.CharField(max_length = 20)
    email = forms.CharField(max_length = 50)
    password = forms.CharField(widget = forms.PasswordInput())
   
    class Meta:
        model =User
        fields=['first_name','last_name','username','email','password']

class SubscriberForm(forms.ModelForm):
    f_name=forms.CharField(max_length = 50,required=False)
    m_name=forms.CharField(max_length = 50,required=False)
    l_name=forms.CharField(max_length = 50,required=False)
    phone_no=forms.IntegerField(required=False)
    date_of_subscribtion=forms.DateField(required=False)
    current_location=forms.CharField(max_length = 50,required=False)
    sex=forms.CharField(max_length = 50,required=False)
    streat=forms.CharField(max_length = 50,required=False)
    state=forms.CharField(max_length = 50,required=False)
    pin=forms.CharField(max_length = 50,required=False)

    class Meta:
        model =Subscriber
        fields=['f_name','m_name','l_name','phone_no']

class ServicesForm(forms.Form):
    plan_no=forms.IntegerField(required=False)
    plan_rate=forms.IntegerField(required=False)
    plan_type=forms.CharField(max_length = 50,required=False)
    office_code=forms.IntegerField(required=False)
    
class ServicesOnPhoneForm(forms.Form):
    phon_no=forms.IntegerField(required=False)
    plan_no=forms.IntegerField(required=False)

class PhoneBookForm(forms.Form):
    phone_no=forms.IntegerField(required=False)
    f_name=forms.CharField(max_length = 50,required=False)
    m_mane=forms.CharField(max_length = 50,required=False)
    l_name=forms.CharField(max_length = 50,required=False)
    location=forms.CharField(max_length = 50,required=False)
    
class PhoneBillForm(forms.Form):
    phone_no=forms.IntegerField(required=False)
    call_duration=forms.IntegerField(required=False)
    call_type=forms.CharField(max_length = 50,required=False)
   # phone=forms.IntegerField(required=False)
    roaming_charges=forms.IntegerField(required=False)
    exchange_no=forms.IntegerField(required=False)
    
class AdministratorForm(forms.ModelForm):
    ssn=forms.IntegerField(required=False)
    streat=forms.CharField(max_length = 50,required=False)
    state=forms.CharField(max_length = 50,required=False)
    pin=forms.IntegerField(required=False)
    f_name=forms.CharField(max_length=50,required=False)
    m_name=forms.CharField(max_length=50,required=False)
    l_name=forms.CharField(max_length=50,required=False)
    salary=forms.IntegerField(required=False)
    sex=forms.CharField(max_length=50,required=False)
    date_of_joining=forms.DateField(required=False)
    
    class Meta:
        model =Administrator
        fields=['ssn','f_name','m_name','l_name','streat','state','pin','salary','sex','date_of_joining']

class TelephoneExchangeForm(forms.Form):
    exchange_no=forms.IntegerField(required=False)
    street=forms.CharField(max_length=50,required=False)
    state=forms.CharField(max_length=50,required=False)
    pin=forms.IntegerField(required=False)
    office_name=forms.CharField(max_length=50,required=False)
    office_code=forms.IntegerField(required=False)
    
class TelephoneOfficeForm(forms.Form):
    office_code=forms.IntegerField(required=False)
    street=forms.CharField(max_length=50,required=False)
    state=forms.CharField(max_length=50,required=False)
    pin=forms.IntegerField(required=False)
    ssn=forms.IntegerField(required=False)
    
class AdminPhoneNoForm(forms.Form):
     phone_no=forms.IntegerField(required=False)
     ssn=forms.IntegerField(required=False)
     
class OfficePhoneForm(forms.Form):
     phone_no=forms.IntegerField(required=False)
     office_code=forms.IntegerField(required=False)
     
class FeaturesForm(forms.Form):
      feature=forms.CharField(max_length=50,required=False)
      plan_no=forms.IntegerField(required=False)
      
class AcessesForm(forms.Form):
      phone_no=forms.IntegerField(required=False)
      plan_no=forms.IntegerField(required=False)
      
class ManagesForm(forms.Form):
     office_code=forms.IntegerField(required=False)
     phone=forms.IntegerField(required=False)
   
class PaybillForm(forms.Form):
      phone_no=forms.IntegerField(required=False)
      phone_no=forms.IntegerField(required=False)
     
class ConnectsForm(forms.Form):
      phone_no=forms.IntegerField(required=False)
      exchange_no=forms.IntegerField(required=False)
      
class TOfficePhoneForm(forms.Form):
    phone_no=forms.IntegerField(required=False)
    
