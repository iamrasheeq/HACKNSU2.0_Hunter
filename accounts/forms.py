from django.forms import ModelForm
from .models import *


class VendorOrderForm(ModelForm):
	class Meta:
		model = Vendor_Order
		fields = '__all__'
class ClientOrderForm(ModelForm):
	class Meta:
		model = Client_Order
		fields = '__all__'

class VendorCreate(ModelForm):
	class Meta:
		model = Vendor
		fields = '__all__'
class ClientCreate(ModelForm):
	class Meta:
		model = Client
		fields = '__all__'
