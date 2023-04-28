from django.contrib import admin
from .models import Metal_detection, Hazard_material, Emp_wellness, UserNew
# Register your models here.
admin.site.register(Metal_detection)
admin.site.register(Hazard_material)
admin.site.register(Emp_wellness)
admin.site.register(UserNew)
