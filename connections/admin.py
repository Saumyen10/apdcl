from django.contrib import admin
from connections.models import Contact,Circle,Division,SubDivision,Consumer,Load

# Register your models here.
admin.site.register(Contact)

admin.site.register(Load)

admin.site.register(Circle)
admin.site.register(Division)
admin.site.register(SubDivision)

admin.site.register(Consumer)