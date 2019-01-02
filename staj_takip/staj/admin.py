from django.contrib import admin
from staj.models import Ogrenci , Staj , Mulakat , Konular , Gun
# Register your models here.


class OgrenciAdmin(admin.ModelAdmin):
    list_display = ('o_isim', 'o_no' , 'o_soyisim' , 'o_ogretim' , 'o_toplam_staj_gunu' , 'ogrenci_dosya')



    class Meta:
        model = Ogrenci

class StajAdmin(admin.ModelAdmin):
    list_display = (
        'kurum_adi', 'sehir' , 'baslama_tarihi' , 'bitis_tarihi' , 'toplam_gun')

    
    class Meta:
        model = Staj

class MulakatAdmin(admin.ModelAdmin):
    list_display = ('staj' , 'mulakat_tarhi', 'mulakat_saati', 'devam' , 'caba_calisma' , 'isi_vaktinde_yapma' , 'davranis' , 'arkadaslara_davranis' , 'proje' , 'duzen' , 'sunum' , 'icerik' , 'mulakat_degerlendirmesi')

    class Meta:
        model = Mulakat

class KonularAdmin(admin.ModelAdmin):
    list_display = ('baslik' ,)

    class Meta:
        model = Konular 

class GunAdmin(admin.ModelAdmin):
    list_display = ('toplam_gun', )
    class Meta:
        Gun

admin.site.register(Ogrenci , OgrenciAdmin)
admin.site.register(Staj , StajAdmin)
admin.site.register(Mulakat , MulakatAdmin)
admin.site.register(Konular ,KonularAdmin)
admin.site.register(Gun , GunAdmin)