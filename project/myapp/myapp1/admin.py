from django.contrib import admin

# Register your models here.
from .models import record_model
from .models import service_info
from .models import blog_model

admin.site.register(record_model)
admin.site.register(service_info)
admin.site.register(blog_model)