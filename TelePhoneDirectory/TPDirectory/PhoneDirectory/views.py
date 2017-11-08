from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import templates
from django.views.generic import View
from .forms import LoginForm,SignUpForm,AdministratorForm,TelephoneOfficeForm,TOfficePhoneForm,TelephoneExchangeForm,SubscriberForm,ManagesForm,FeaturesForm,ConnectsForm,ServicesForm,ServicesOnPhoneForm,PhoneBookForm,PhoneBillForm,AdminPhoneNoForm
from django.contrib.auth import authenticate, login,logout
from .models import Administrator,Subscriber,Services,TelephoneOffice,Manages,TelephoneExchange,TOfficePhone,Features,ServiceOnPhones,PhoneBook,PhoneBill,AdminPhoneNo,Connect

from django.views.generic import View
def hello(request):   
   return render(request, 'home.html',)

def dashboard(request):  
    if request.method=='GET':
        return render(request,'dashboard.html')
        
    if request.method=='POST' and 'btnform' in request.POST:
        return render(request,'home.html')
        
    if request.method=='POST' and 'btnform1' in request.POST:
        Subs_form=SubscriberForm(request.POST,prefix='Subscriber')
        if Subs_form.is_valid():
            a=Subs_form.cleaned_data['f_name']
            
            Object=Subscriber.objects.all()
            return render(request, 'dashboard.html',{'Subs_form':Subs_form,'Object':Object})
            
    elif request.method=='POST' and 'btnform2' in request.POST:        
        Services_form=ServicesForm(request.POST,prefix='Services')
        if Services_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object1=Services.objects.all()
            return render(request, 'dashboard.html',{'Services_form':Services_form,'Object1':Object1})
    
    elif request.method=='POST' and 'btnform3' in request.POST:        
        Serviceop_form=ServicesOnPhoneForm(request.POST,prefix='ServicesOnPhone')
        if Serviceop_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object2=ServiceOnPhones.objects.all()
            return render(request, 'dashboard.html',{'Serviceop_form':Serviceop_form,'Object2':Object2})
    
    elif request.method=='POST' and 'btnform4' in request.POST:        
        PB_form=PhoneBookForm(request.POST,prefix='PhoneBook')
        if PB_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object3=PhoneBook.objects.all()
            return render(request, 'dashboard.html',{'PB_form':PB_form,'Object3':Object3})
    
    elif request.method=='POST' and 'btnform5' in request.POST:        
        PBL_form=PhoneBillForm(request.POST,prefix='PhoneBill')
        if PBL_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object4=PhoneBill.objects.all()
            return render(request, 'dashboard.html',{'PBL_form':PBL_form,'Object4':Object4})
    
    elif request.method=='POST' and 'btnform6' in request.POST:        
        Adphones_form=AdminPhoneNoForm(request.POST,prefix='AdminPhoneNo')
        if Adphones_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object5=AdminPhoneNo.objects.all()
            return render(request, 'dashboard.html',{'Adphones_form':Adphones_form,'Object5':Object5})
    
    elif request.method=='POST' and 'btnform7' in request.POST:        
        Connects_form=ConnectsForm(request.POST,prefix='Connects')
        if Connects_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object6=Connect.objects.all()
            return render(request, 'dashboard.html',{'Connects_form':Connects_form,'Object6':Object6})
            
    elif request.method=='POST' and 'btnform8' in request.POST:        
        Features_form=FeaturesForm(request.POST,prefix='Features')
        if Features_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object7=Features.objects.all()
            return render(request, 'dashboard.html',{'Features_form':Features_form,'Object7':Object7})
            
    elif request.method=='POST' and 'btnform9' in request.POST:        
        Manages_form=ManagesForm(request.POST,prefix='Manages')
        if Manages_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object8=Manages.objects.all()
            return render(request, 'dashboard.html',{'Manages_form':Manages_form,'Object8':Object8})
            
    elif request.method=='POST' and 'btnform10' in request.POST:        
        TOfficePhone_form=TOfficePhoneForm(request.POST,prefix='TOfficePhone')
        if TOfficePhone_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object9=TOfficePhone.objects.all()
            return render(request, 'dashboard.html',{'TOfficePhone_form':TOfficePhone_form,'Object9':Object9}) 
    
    elif request.method=='POST' and 'btnform11' in request.POST:        
        TelephoneExchange_form=TelephoneExchangeForm(request.POST,prefix='TelephoneExchange')
        if TelephoneExchange_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object10=TelephoneExchange.objects.all()
            return render(request, 'dashboard.html',{'TelephoneExchange_form':TelephoneExchange_form,'Object10':Object10}) 

    elif request.method=='POST' and 'btnform12' in request.POST:        
        TelephoneOffice_form=TelephoneOfficeForm(request.POST,prefix='TelephoneOffice')
        if TelephoneOffice_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object11=TelephoneOffice.objects.all()
            return render(request, 'dashboard.html',{'TelephoneOffice_form':TelephoneOffice_form,'Object11':Object11}) 

    elif request.method=='POST' and 'btnform13' in request.POST:        
        Administrator_form=AdministratorForm(request.POST,prefix='Administrator')
        if Administrator_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object12=Administrator.objects.all()
            return render(request, 'dashboard.html',{'Administrator_form':Administrator_form,'Object12':Object12})            
    
    form=SubscriberForm()    
        #logout(request)
        #return redirect('hello')
    return render(request,'dashboard.html',{'form':form}) 

def AdminUpdate(request):
    if request.method=='GET':
        return render(request,'admindash.html')
    if request.method=='POST' and 'btnform1' in request.POST:
        Subs_form=SubscriberForm(request.POST,prefix='Subscriber')
        if Subs_form.is_valid(): 
            #user=Subs_form.save(commit=False)
            
            #cleaned normalized data
            f_name=Subs_form.cleaned_data['f_name']
            m_name=Subs_form.cleaned_data['m_name']
            l_name=Subs_form.cleaned_data['l_name']
           # phone_no=Subs_form.cleaned_data['phone_no']
            date_of_subscribtion=Subs_form.cleaned_data['date_of_subscribtion']
            current_location=Subs_form.cleaned_data['current_location']
            sex=Subs_form.cleaned_data['sex']
            streat=Subs_form.cleaned_data['streat']
            state=Subs_form.cleaned_data['state']
            pin=Subs_form.cleaned_data['pin']
           # email=form.cleaned_data['email']
           # password=form.cleaned_data['password']
            #user.set_password(password)
            Object=Subscriber.objects.all().filter(f_name=f_name)
            for obj in Object:
                obj.f_name=f_name
                obj.m_name=m_name
                obj.l_name=l_name
                obj.date_of_subscribtion=date_of_subscribtion
                obj.current_location=current_location
                obj.sex=sex
                obj.streat=streat
                obj.state=state
                obj.pin
                #obj.phone_no=phone_no
                obj.save()
            #user.save()
            #return redirect('hello')
            # returns user objetcs if credentials are corect
        
            Object=Subscriber.objects.all()
            return render(request, 'admindash.html',{'Subs_form':Subs_form,'Object':Object})
            
    elif request.method=='POST' and 'btnform2' in request.POST:        
        Services_form=ServicesForm(request.POST,prefix='Services')
        if Services_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object1=Services.objects.all()
            return render(request, 'admindash.html',{'Services_form':Services_form,'Object1':Object1})
    
    elif request.method=='POST' and 'btnform3' in request.POST:        
        Serviceop_form=ServicesOnPhoneForm(request.POST,prefix='ServicesOnPhone')
        if Serviceop_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object2=ServiceOnPhones.objects.all()
            return render(request, 'admindash.html',{'Serviceop_form':Serviceop_form,'Object2':Object2})
    
    elif request.method=='POST' and 'btnform4' in request.POST:        
        PB_form=PhoneBookForm(request.POST,prefix='PhoneBook')
        if PB_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object3=PhoneBook.objects.all()
            return render(request, 'admindash.html',{'PB_form':PB_form,'Object3':Object3})
    
    elif request.method=='POST' and 'btnform5' in request.POST:        
        PBL_form=PhoneBillForm(request.POST,prefix='PhoneBill')
        if PBL_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object4=PhoneBill.objects.all()
            return render(request, 'admindash.html',{'PBL_form':PBL_form,'Object4':Object4})
    
    elif request.method=='POST' and 'btnform6' in request.POST:        
        Adphones_form=AdminPhoneNoForm(request.POST,prefix='AdminPhoneNo')
        if Adphones_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object5=AdminPhoneNo.objects.all()
            return render(request, 'admindash.html',{'Adphones_form':Adphones_form,'Object5':Object5})
    
    elif request.method=='POST' and 'btnform7' in request.POST:        
        Connects_form=ConnectsForm(request.POST,prefix='Connects')
        if Connects_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object6=Connect.objects.all()
            return render(request, 'admindash.html',{'Connects_form':Connects_form,'Object6':Object6})
            
    elif request.method=='POST' and 'btnform8' in request.POST:        
        Features_form=FeaturesForm(request.POST,prefix='Features')
        if Features_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object7=Features.objects.all()
            return render(request, 'admindash.html',{'Features_form':Features_form,'Object7':Object7})
            
    elif request.method=='POST' and 'btnform9' in request.POST:        
        Manages_form=ManagesForm(request.POST,prefix='Manages')
        if Manages_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object8=Manages.objects.all()
            return render(request, 'admindash.html',{'Manages_form':Manages_form,'Object8':Object8})
            
    elif request.method=='POST' and 'btnform10' in request.POST:        
        TOfficePhone_form=TOfficePhoneForm(request.POST,prefix='TOfficePhone')
        if TOfficePhone_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object9=TOfficePhone.objects.all()
            return render(request, 'admindash.html',{'TOfficePhone_form':TOfficePhone_form,'Object9':Object9}) 
    
    elif request.method=='POST' and 'btnform11' in request.POST:        
        TelephoneExchange_form=TelephoneExchangeForm(request.POST,prefix='TelephoneExchange')
        if TelephoneExchange_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object10=TelephoneExchange.objects.all()
            return render(request, 'admindash.html',{'TelephoneExchange_form':TelephoneExchange_form,'Object10':Object10}) 

    elif request.method=='POST' and 'btnform12' in request.POST:        
        TelephoneOffice_form=TelephoneOfficeForm(request.POST,prefix='TelephoneOffice')
        if TelephoneOffice_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object11=TelephoneOffice.objects.all()
            return render(request, 'admindash.html',{'TelephoneOffice_form':TelephoneOffice_form,'Object11':Object11}) 

    elif request.method=='POST' and 'btnform13' in request.POST:        
        Administrator_form=AdministratorForm(request.POST,prefix='Administrator')
        if Administrator_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            ssn=Administrator_form.cleaned_data['ssn']
            f_name=Administrator_form.cleaned_data['f_name']
            m_name=Administrator_form.cleaned_data['m_name']
            l_name=Administrator_form.cleaned_data['l_name']
            streat=Administrator_form.cleaned_data['streat']
            state=Administrator_form.cleaned_data['state']
            pin=Administrator_form.cleaned_data['pin']
            salary=Administrator_form.cleaned_data['salary']
            sex=Administrator_form.cleaned_data['sex']
           # date_of_joining=Administrator_form.cleaned_data['date_of_joining']
           # email=form.cleaned_data['email']
           # password=form.cleaned_data['password']
            #user.set_password(password)
            Object=Administrator.objects.all().filter(ssn=ssn)
            for obj in Object:
                obj.f_name=f_name
                obj.m_name=m_name
                obj.l_name=l_name
                obj.streat=streat
                obj.state=state
                obj.pin=pin
                obj.date_of_joining=date_of_joining
                obj.salary=salary
                obj.sex=sex
                #obj.phone_no=phone_no
                obj.save()
            
            Object12=Administrator.objects.all()
            return render(request, 'admindash.html',{'Administrator_form':Administrator_form,'Object12':Object12})            
    
   # form=SubscriberForm()    
        #logout(request)
        #return redirect('hello')
    #return render(request,'admindash.html',{'form':form})  

def Administratore(request):  
    if request.method=='GET':
        return render(request,'admindash.html')
    if request.method=='POST' and 'btnform1' in request.POST:
        Subs_form=SubscriberForm(request.POST,prefix='Subscriber')
        if Subs_form.is_valid():
            a=Subs_form.cleaned_data['f_name']
            b=Subs_form.cleaned_data['m_name']
            c=Subs_form.cleaned_data['l_name']
            p=Subs_form.cleaned_data['phone_no']
            
            if a:
                Object=Subscriber.objects.all().filter(f_name=a)
                return render(request, 'admindash.html',{'Subs_form':Subs_form,'Object':Object})
            elif b :
                Object=Subscriber.objects.all().filter(m_name=b)
                return render(request, 'admindash.html',{'Subs_form':Subs_form,'Object':Object})                
            elif p :
                Object=Subscriber.objects.all().filter(phone_no=p)
                return render(request, 'admindash.html',{'Subs_form':Subs_form,'Object':Object})
             
    elif request.method=='POST' and 'btnform2' in request.POST:        
        Services_form=ServicesForm(request.POST,prefix='Services')
        if Services_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object1=Services.objects.all()
            return render(request, 'admindash.html',{'Services_form':Services_form,'Object1':Object1})
    
    elif request.method=='POST' and 'btnform3' in request.POST:        
        Serviceop_form=ServicesOnPhoneForm(request.POST,prefix='ServicesOnPhone')
        if Serviceop_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object2=ServiceOnPhones.objects.all()
            return render(request, 'admindash.html',{'Serviceop_form':Serviceop_form,'Object2':Object2})
    
    elif request.method=='POST' and 'btnform4' in request.POST:        
        PB_form=PhoneBookForm(request.POST,prefix='PhoneBook')
        if PB_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object3=PhoneBook.objects.all()
            return render(request, 'admindash.html',{'PB_form':PB_form,'Object3':Object3})
    
    elif request.method=='POST' and 'btnform5' in request.POST:        
        PBL_form=PhoneBillForm(request.POST,prefix='PhoneBill')
        if PBL_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object4=PhoneBill.objects.all()
            return render(request, 'admindash.html',{'PBL_form':PBL_form,'Object4':Object4})
    
    elif request.method=='POST' and 'btnform6' in request.POST:        
        Adphones_form=AdminPhoneNoForm(request.POST,prefix='AdminPhoneNo')
        if Adphones_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object5=AdminPhoneNo.objects.all()
            return render(request, 'admindash.html',{'Adphones_form':Adphones_form,'Object5':Object5})
    
    elif request.method=='POST' and 'btnform7' in request.POST:        
        Connects_form=ConnectsForm(request.POST,prefix='Connects')
        if Connects_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object6=Connect.objects.all()
            return render(request, 'admindash.html',{'Connects_form':Connects_form,'Object6':Object6})
            
    elif request.method=='POST' and 'btnform8' in request.POST:        
        Features_form=FeaturesForm(request.POST,prefix='Features')
        if Features_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object7=Features.objects.all()
            return render(request, 'admindash.html',{'Features_form':Features_form,'Object7':Object7})
            
    elif request.method=='POST' and 'btnform9' in request.POST:        
        Manages_form=ManagesForm(request.POST,prefix='Manages')
        if Manages_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object8=Manages.objects.all()
            return render(request, 'admindash.html',{'Manages_form':Manages_form,'Object8':Object8})
            
    elif request.method=='POST' and 'btnform10' in request.POST:        
        TOfficePhone_form=TOfficePhoneForm(request.POST,prefix='TOfficePhone')
        if TOfficePhone_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object9=TOfficePhone.objects.all()
            return render(request, 'admindash.html',{'TOfficePhone_form':TOfficePhone_form,'Object9':Object9}) 
    
    elif request.method=='POST' and 'btnform11' in request.POST:        
        TelephoneExchange_form=TelephoneExchangeForm(request.POST,prefix='TelephoneExchange')
        if TelephoneExchange_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object10=TelephoneExchange.objects.all()
            return render(request, 'admindash.html',{'TelephoneExchange_form':TelephoneExchange_form,'Object10':Object10}) 

    elif request.method=='POST' and 'btnform12' in request.POST:        
        TelephoneOffice_form=TelephoneOfficeForm(request.POST,prefix='TelephoneOffice')
        if TelephoneOffice_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object11=TelephoneOffice.objects.all()
            return render(request, 'admindash.html',{'TelephoneOffice_form':TelephoneOffice_form,'Object11':Object11}) 

    elif request.method=='POST' and 'btnform13' in request.POST:        
        Administrator_form=AdministratorForm(request.POST,prefix='Administrator')
        if Administrator_form.is_valid():
            #a=Services_form.cleaned_data['f_name']
            
            Object12=Administrator.objects.all()
            return render(request, 'admindash.html',{'Administrator_form':Administrator_form,'Object12':Object12})            
    
    form=SubscriberForm()    
        #logout(request)
        #return redirect('hello')
    return render(request,'admindash.html',{'form':form}) 
       
def userupdate(request):

    form_class = SignUpForm
    template_name = 'signup.html'
    
    def get(self, request):
        form=self.form_class(None)
        return redirect('SignUpFormView.as_view()', {'form':form})
        
    #process form data

    def post(self, request):
        form= self.form_class(request.POST)
        
        if form.is_valid():
            user=form.save(commit=False)
            
            #cleaned normalized data
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #return redirect('hello')
            # returns user objetcs if credentials are corect
            user=authenticate(username=username,password=password)
                 
            return redirect('dashboard')
       
        return render('SignUpFormView.as_view()', {'form':form})

def signin(request):
    #template_name = 'signin.html'
    
    #display blank form
    if request.method=='GET':
        return render(request, 'signin.html', )
        
    #process form data
    if request.method=='POST':
            #user=form.save(commit=False)
            #return render(request, 'home.html',)
            #cleaned normalized data
        username=request.POST['username']
        password=request.POST['password']
           # user.set_password(password)
            #user.save()
            # returns user objetcs if credentials are corect
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('dashboard')
            
    return redirect('signup')

def adminsignin(request):
    #template_name = 'signin.html'
    
    #display blank form
    if request.method=='GET':
        return render(request, 'signin.html', )
                
    if request.method=='POST':
            #user=form.save(commit=False)
            #return render(request, 'home.html',)
            #cleaned normalized data
        username=request.POST['username']
        password=request.POST['password']
           # user.set_password(password)
            #user.save()
            # returns user objetcs if credentials are corect
        user=authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('Administratore')
        return redirect('signup')

class SignUpFormView(View):
    form_class = SignUpForm
    template_name = 'signup.html'
    
    #display blank form
    def get(self, request):
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form})
        
    #process form data

    def post(self, request):
        form= self.form_class(request.POST)
        
        if form.is_valid():
            user=form.save(commit=False)
            
            #cleaned normalized data
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            #return redirect('hello')
            # returns user objetcs if credentials are corect
            user=authenticate(username=username,password=password)
            
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('dashboard')
                
        
        return render(request, self.template_name, {'form':form})



        
#return redirect('hello')
# Create your views here.
