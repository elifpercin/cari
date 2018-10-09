from django.contrib import admin

# Register your models here.
from.models import Post, Category, Ogretmen,Dersler,Ucret,Odeme
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Ogretmen)
admin.site.register(Dersler)
admin.site.register(Ucret)
admin.site.register(Odeme)