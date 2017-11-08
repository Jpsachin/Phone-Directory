# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AdminPhoneNo(models.Model):
    phone_no = models.AutoField(db_column='Phone_no', primary_key=True)  # Field name made lowercase.
    ssn = models.ForeignKey('Administrator', models.DO_NOTHING, db_column='SSN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_phone_no'

    def __str__(self):
        return '%s' % self.phone_no

class Administrator(models.Model):
    ssn = models.IntegerField(db_column='SSN', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(db_column='F_name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    m_name = models.CharField(db_column='M_name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    streat = models.CharField(db_column='Streat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pin = models.IntegerField(db_column='PIN', blank=True, null=True)  # Field name made lowercase.
    sex = models.CharField(db_column='Sex', max_length=6, blank=True, null=True)  # Field name made lowercase.
    date_of_joining = models.DateField(db_column='Date_of_joining', blank=True, null=True)  # Field name made lowercase.
    salary = models.IntegerField(db_column='Salary', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'administrator'
    
    def __str__(self):
        return '%s' % self.ssn

"""
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)
"""

class Connect(models.Model):
    phone_no = models.ForeignKey('Subscriber', models.DO_NOTHING, db_column='Phone_no',  primary_key=True)  # Field name made lowercase.
    exchange_no = models.ForeignKey('TelephoneExchange', models.DO_NOTHING, db_column='Exchange_no', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'connect'

    def __str__(self):
        return '%s' % self.phone_no
    
    
"""
class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
"""

class Features(models.Model):
    feature = models.CharField(max_length=25, primary_key=True)
    plan_no = models.ForeignKey('Services', models.DO_NOTHING, db_column='Plan_no', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'features'
        
    def __str__(self):
        return '%s' % self.plan_no

class Manages(models.Model):
    office_code = models.ForeignKey('TelephoneOffice', models.DO_NOTHING, db_column='Office_code',primary_key=True)  # Field name made lowercase.
    phone_no = models.ForeignKey('PhoneBook', models.DO_NOTHING, db_column='Phone_no', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'manages'

    def __str__(self):
        return '%s' % self.phone_no

class PhoneBill(models.Model):
    phone_no = models.ForeignKey('PhoneBook', models.DO_NOTHING, db_column='phone_no',primary_key=True)  # Field name made lowercase.
    call_duration = models.IntegerField(blank=True, null=True)
    call_type = models.CharField(max_length=15, blank=True, null=True)
    roaming_charges = models.IntegerField(blank=True, null=True)
    exchange_no = models.ForeignKey('TelephoneExchange', models.DO_NOTHING, db_column='Exchange_no', blank=True, null=True)  # Field name made lowercase.
    #phone_no = models.IntegerField(db_column='Phone_no', primary_key=True)
    class Meta:
        managed = False
        db_table = 'phone_bill'

    def __str__(self):
        return '%s' % self.phone_no

class PhoneBook(models.Model):
    phone_no = models.AutoField(db_column='Phone_no', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(db_column='F_name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    m_name = models.CharField(db_column='M_name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=15, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phone_book'

    def __str__(self):
        return '%s' % self.phone_no

class ServiceOnPhones(models.Model):
    phon_no = models.AutoField(db_column='Phon_no', primary_key=True)  # Field name made lowercase.
    plan_no = models.ForeignKey('Services', models.DO_NOTHING, db_column='Plan_no', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service_on_phones'
    
    def __str__(self):              # __unicode__ on Python 2
        return '%s' % self.phon_no


class Services(models.Model):
    plan_no = models.IntegerField(db_column='Plan_no', primary_key=True)  # Field name made lowercase.
    plan_rate = models.CharField(db_column='Plan_rate', max_length=10, blank=True, null=True)  # Field name made lowercase.
    plan_type = models.CharField(db_column='Plan_type', max_length=20, blank=True, null=True)  # Field name made lowercase.
    office_code = models.ForeignKey('TelephoneOffice', models.DO_NOTHING, db_column='Office_code', blank=True, null=True)  # Field name made lowercase.
    #phon_no = models.AutoField(db_column='Phon_no', primary_key=True)
    
    class Meta:
        managed = False
        db_table = 'services'

    def __str__(self):              # __unicode__ on Python 2
        return '%s' % self.plan_no

class Subscriber(models.Model):
    phone_no = models.ForeignKey(PhoneBook, models.DO_NOTHING, db_column='Phone_no', primary_key=True)  # Field name made lowercase.
    f_name = models.CharField(db_column='F_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    m_name = models.CharField(db_column='M_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    l_name = models.CharField(db_column='L_name', max_length=10, blank=True, null=True)  # Field name made lowercase.
    date_of_subscribtion = models.DateField(db_column='Date_of_subscribtion', blank=True, null=True)  # Field name made lowercase.
    current_location = models.CharField(max_length=30, blank=True, null=True)
    sex = models.CharField(max_length=6, blank=True, null=True)
    streat = models.CharField(db_column='Streat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pin = models.IntegerField(db_column='PIN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subscriber'
        
    def __str__(self):
        return '%s' % self.phone_no


class TOfficePhone(models.Model):
    phone_no = models.AutoField(db_column='Phone_no', primary_key=True)  # Field name made lowercase.
    office_code = models.ForeignKey('TelephoneOffice', models.DO_NOTHING, db_column='Office_code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_office_phone'

    def __str__(self):
        return '%s' % self.phone_no

class TelephoneExchange(models.Model):
    exchange_no = models.IntegerField(db_column='Exchange_no', primary_key=True)  # Field name made lowercase.
    streat = models.CharField(db_column='Streat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pin = models.IntegerField(db_column='PIN', blank=True, null=True)  # Field name made lowercase.
    office_name = models.CharField(db_column='Office_name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    office_code = models.ForeignKey('TelephoneOffice', models.DO_NOTHING, db_column='Office_code', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telephone_exchange'

    def __str__(self):
        return '%s' % self.exchange_no

class TelephoneOffice(models.Model):
    office_code = models.IntegerField(db_column='Office_code', primary_key=True)  # Field name made lowercase.
    streat = models.CharField(db_column='Streat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pin = models.IntegerField(db_column='PIN', blank=True, null=True)  # Field name made lowercase.
    ssn = models.ForeignKey(Administrator, models.DO_NOTHING, db_column='SSN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'telephone_office'

    def __str__(self):
        return '%s' % self.office_code