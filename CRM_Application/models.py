from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=25,blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=50, default='user')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.username
    
class Contact(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=50)
    owner_user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.name
    
class Campaign(models.Model):
    campaign_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.DecimalField(max_digits=10,decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class ContactCampaign(models.Model):
    contact_id = models.ForeignKey(Contact, on_delete=models.CASCADE)
    campaign_id = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    def __str__(self):
        return f"{self.contact} in {self.campaign}"

class Session(models.Model):
    session_id = models.BigIntegerField(primary_key=True)
    contact_id = models.ForeignKey(Contact, on_delete=models.SET_NULL, null=True)
    session_start = models.DateTimeField()
    session_end = models.DateField()
    app_version = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)
    traffic_source = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    def __str__(self):
        return str(self.session_id)
    
class Item(models.Model):
    item_id = models.IntegerField(primary_key=True)
    item_category = models.CharField(max_length=100)
    item_name = models.CharField(max_length=255)
    def __self__(self):
        return self.item_name
    
class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    session_id = models.ForeignKey(Session, on_delete=models.CASCADE)
    event_time = models.DateTimeField()
    event_name = models.CharField(max_length=50)
    item_id = models.ForeignKey(Item, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.event_name
    



class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")