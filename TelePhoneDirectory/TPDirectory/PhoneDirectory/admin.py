from django.contrib import admin

from .models import Administrator
from .models import AdminPhoneNo
from .models import Connect
from .models import Features
from .models import Manages
from .models import PhoneBill
from .models import PhoneBook
from .models import ServiceOnPhones
from .models import Services
from .models import Subscriber
from .models import TOfficePhone
from .models import TelephoneExchange
from .models import TelephoneOffice
admin.site.register(Administrator)
admin.site.register(AdminPhoneNo)
admin.site.register(Connect)
admin.site.register(Features)
admin.site.register(Manages)
admin.site.register(PhoneBill)
admin.site.register(PhoneBook)
admin.site.register(ServiceOnPhones)
admin.site.register(Services)
admin.site.register(Subscriber)
admin.site.register(TOfficePhone)
admin.site.register(TelephoneExchange)
admin.site.register(TelephoneOffice)
# Register your models here.
