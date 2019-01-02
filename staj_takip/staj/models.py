from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator
from django.core.exceptions import ValidationError


class Ogrenci(models.Model):

    OGRETIMLER = (
        ('1.' , '1'),
        ('2.' , '2'),
    )

    o_isim = models.CharField(verbose_name ="Öğrenci Adı" , max_length=50)
    o_soyisim = models.CharField(verbose_name = "Öğrenci Soyadı" , max_length=50)
    o_sinif = models.IntegerField(verbose_name="Sınıfı")
    o_no = models.IntegerField(verbose_name="Öğrenci No" , unique=True)
    o_ogretim = models.CharField(verbose_name = "Öğretim" ,max_length = 2, choices = OGRETIMLER)
    o_toplam_staj_gunu = models.IntegerField(verbose_name = "Toplam Staj Günü" , default=0 , validators = [MinValueValidator(0)])
    staj_tamamadi_mi = models.BooleanField(verbose_name = "Staj Tamamlandı mı ?" , default = False)
    staj_sayisi = models.IntegerField(default=0 , null=True)
    dgs_veya_yatay_mi = models.BooleanField(default = False)
    onceki_okul = models.CharField(max_length=50 , null = True , blank = True)
    ogrenci_dosya = models.FileField(null = True , blank = True)
    staj_gunu = models.IntegerField(default=0 , null = True )

    #handling dgs and yatay gecis students their first school 
    def clean(self):
        if self.dgs_veya_yatay_mi == False and self.onceki_okul is not None:
            raise ValidationError("Sadece DGS veya Yatay geçiş öğrencileri önceki okul ekleyebilir")
        elif self.dgs_veya_yatay_mi == True and self.onceki_okul is None :
            raise ValidationError("Lütfen önceki okulu giriniz")
    def save(self, *args,**kwargs):
        if self.onceki_okul and self.dgs_veya_yatay_mi:
            self.o_isim = self.o_isim.upper()
            self.o_soyisim = self.o_soyisim.upper()
            self.onceki_okul = self.onceki_okul.upper()
            
        super(Ogrenci, self).save(*args,**kwargs)

    def __str__(self):
        return '%s %s' % (self.o_isim, self.o_soyisim)
    
    

class Staj(models.Model):

    SINIFLAR = (
        ('1,' , '1'),
        ('2,' , '2'),
        ('3,' , '3'),
        ('4,' , '4'),
    )
    
    ogrenci = models.ForeignKey("Ogrenci" ,on_delete=models.CASCADE)
    onceki_staj = models.BooleanField(default=False ,verbose_name = "Önceki staj mı ?" )
    konu = models.ForeignKey("Konular" ,on_delete=models.SET_NULL , null = True , blank = True)  
    kurum_adi = models.CharField(max_length = 200 , verbose_name = "Kurum Adı")
    departman_adi = models.CharField(max_length  =200 , null = True , blank = True , verbose_name = "Departman Adı")
    sinif_durumu = models.CharField(max_length = 50,choices = SINIFLAR , null = True , blank = True , verbose_name = "Sınıf Durumu")
    sehir = models.CharField(max_length = 50 , null = True ,  blank = True, verbose_name = "Şehir")
    baslama_tarihi = models.DateField(null = True , blank = True , verbose_name="Başlama Tarihi")
    bitis_tarihi = models.DateField(null = True , blank = True , verbose_name="Bitiş Tarihi")
    toplam_gun = models.PositiveIntegerField(default = 0 , validators = [MinValueValidator(15)] , verbose_name = "Toplam Gün") 
    gorusme_eklendi_mi = models.BooleanField(default = False , null = True) 
    degerlendirildi = models.BooleanField(default = False)
    
    
    def save(self, *args,**kwargs):
        if self.departman_adi is not None and self.sehir is not None :
            self.kurum_adi = self.kurum_adi.upper()
            self.departman_adi = self.departman_adi.upper()
            self.sehir = self.sehir.upper()
        super(Staj, self).save(*args,**kwargs)
        

class Mulakat(models.Model):
    ANKET = (
        (1 , 1),
        (2 , 2),
        (3 , 3),
        (4,  4),
        (5,  5),
    )

    staj = models.OneToOneField(Staj , on_delete= models.CASCADE)
    mulakat_tarhi = models.DateField(verbose_name="Mulakat Tarihi")
    mulakat_saati = models.TimeField(verbose_name="Mulakat Saati")
    devam = models.PositiveIntegerField(choices=ANKET , verbose_name="Staja Devam")
    caba_calisma = models.PositiveIntegerField(choices=ANKET ,verbose_name="Çaba ve Çalışma")
    isi_vaktinde_yapma = models.PositiveIntegerField(choices=ANKET , verbose_name="İşi vaktinde tamamlama")
    davranis = models.PositiveIntegerField(choices=ANKET , verbose_name="Amire karşı darvranış")
    arkadaslara_davranis = models.PositiveIntegerField(choices=ANKET ,verbose_name="İş arkadaşlarına karşı davranış")
    proje = models.PositiveIntegerField(verbose_name="Proje" , validators = [MinValueValidator(0) , MaxValueValidator(100)])
    duzen = models.PositiveIntegerField(verbose_name="Düzen" , validators = [MinValueValidator(0) , MaxValueValidator(100)])
    sunum = models.PositiveIntegerField(verbose_name="Sunum" , validators = [MinValueValidator(0) , MaxValueValidator(100)])
    icerik = models.PositiveIntegerField(verbose_name="İçerik" , validators = [MinValueValidator(0) , MaxValueValidator(100)])
    mulakat_degerlendirmesi = models.PositiveIntegerField(verbose_name="Mülakat" , validators = [MinValueValidator(0) , MaxValueValidator(100)])
    



class Konular(models.Model):
    baslik = models.CharField(max_length = 50)

    def save(self, *args,**kwargs):
        self.baslik = self.baslik.upper()
        super(Konular, self).save(*args,**kwargs)
    
    def __str__(self):
        return '%s ' % (self.baslik )


class Komisyon(models.Model):

    """ hocalar tablosu oluşturusak daha verimli olabilir """
    """ eklemeler olacak """

    uye1_isim = models.CharField(max_length = 200)
    uye1_soyisim = models.CharField(max_length = 200)
    uye2_isim = models.CharField(max_length = 200)    
    uye2_soyisim = models.CharField(max_length = 200)

    def save(self, *args,**kwargs):
    
        self.uye1_isim = self.uye1_isim.upper()
        self.uye1_soyisim = self.uye1_soyisim.upper()
        self.uye2_isim = self.uye2_isim.upper()
        self.uye2_soyisim = self.uye2_soyisim.upper()

        super(Komisyon, self).save(*args,**kwargs)
    
    def __unicode__(self):
        return  self.uye1_isim + " " +  self.uye2_isim
    def __str__(self):
        return  self.uye1_isim + self.uye2_isim


class Gorusme(models.Model):
    staj = models.OneToOneField(Staj , on_delete= models.CASCADE)
    gorusme_tarihi = models.DateField(verbose_name="Görüşme Tarihi" , null = False)
    gorusme_saati = models.TimeField(verbose_name="Görüşme Saati" , null = False)
    komisyon = models.ForeignKey("Komisyon" ,on_delete=models.SET_NULL , null = True)
    gorusme_yapıldı_mı = models.BooleanField(default  = False) 



class Gun(models.Model):
    toplam_gun = models.PositiveIntegerField(default = 57 , verbose_name = "Tamamlanması gereken gün sayısı")