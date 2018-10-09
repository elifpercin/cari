from django.db import models
from datetime import datetime, timedelta


# Create your models here.


class Category(models.Model):
    kategori_adi = models.CharField(max_length=3000)

    def __str__(self):
        return "%s" % self.kategori_adi

    class Meta:
        verbose_name_plural = 'Kategoriler'


class Ogretmen(models.Model):
    icerik_adi = models.CharField(max_length=240)

    def __str__(self):
        return "%s" % self.icerik_adi

    class Meta:
        verbose_name_plural = 'Öğretmenler'


class Dersler(models.Model):
    ders_adi = models.CharField(max_length=100, default='', verbose_name='Ders Adi')
    kategori = models.ManyToManyField(Category, verbose_name='Ders', help_text='Ders seçiniz')

    class Meta:
        verbose_name_plural = 'Dersler'

    def __str__(self):
        return self.ders_adi


class Ucret(models.Model):
    ders = models.ForeignKey(Dersler,related_name='ders',on_delete=models.CASCADE,null=True, blank=False,verbose_name='Ders')
    ucret = models.IntegerField(null=False, verbose_name='Ucret', default=0)






    class Meta:
        verbose_name_plural = 'Ucret'


class Odeme(models.Model):
    alinan_dersler=models.OneToOneField(Dersler,related_name='alinan_dersler',on_delete=models.CASCADE,null=True,blank=False)
    odeme=models.IntegerField(null=False,verbose_name='Odeme',default=0)

    def __str__(self):
        return "%s" % self.alinan_dersler

    class Meta:
        verbose_name_plural = 'Odeme'



class Post(models.Model):
    title = models.CharField(max_length=250, blank=False, verbose_name='Ad ve Soyad Giriniz')
    ders = models.ForeignKey(to=Dersler, null=True, blank=False, verbose_name='Dersler',on_delete=models.CASCADE)
    icerik = models.ManyToManyField(Ogretmen, verbose_name='Öğretmen', help_text='Öğretmen Seçiniz')
    draft = models.BooleanField(default=False, verbose_name='Taslak olusturulsun mu?')
    img=models.ImageField(blank=True,verbose_name='Resim')
    created_date = models.DateTimeField(auto_now_add=True)  # sadece ilk oluşturulduğunda
    updated_date = models.DateTimeField(auto_now=True)  # her kayıt işleminde
    Tarih = models.DateTimeField(default=datetime.now() + timedelta(days=30))

    def __str__(self):
        return "%s" % (self.title)

    class Meta:
        verbose_name_plural = 'Gönderiler'
        ordering = ['created_date']  # oluşturulan zamana göre sıralama yapar




