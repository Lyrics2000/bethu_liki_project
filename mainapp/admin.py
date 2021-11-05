from django.contrib import admin
from .models import (
    Passengers,
    Gate,
    Flights,
    Tempereture
)

# Register your models here.
admin.site.register(Passengers)
admin.site.register(Gate)
admin.site.register(Flights)
admin.site.register(Tempereture)



