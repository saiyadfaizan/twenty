from django.db import models

from store.models import *
# Create your models here.
from store.models import Admin

print(Admin.objects.all())