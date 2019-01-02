from django import forms


from .models import Ogrenci , Staj , Konular , Mulakat , Komisyon , Gorusme , Gun
class OgrenciForm(forms.ModelForm):

    class Meta:
        model = Ogrenci
        
        fields = [
            'o_isim',
            'o_soyisim',
            'o_no',
            'o_ogretim',
            'o_sinif',
            'dgs_veya_yatay_mi',
            'onceki_okul',
        ]
class OgrenciDosyaForm(forms.ModelForm):
    class Meta:
        model = Ogrenci
        fields = [
                'ogrenci_dosya'
        ]
        
class StajForm(forms.ModelForm):

    
    class Meta : 
        model = Staj

        fields = [
            'onceki_staj',
            'konu',
            'kurum_adi',
            'departman_adi',
            'sinif_durumu',
            'sehir',
            'konu',
            'baslama_tarihi',
            'bitis_tarihi',
            'toplam_gun',
        ]
        widgets = {
            'baslama_tarihi': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'Select a date' ,
                                            'type' : 'date'}) , 
            'bitis_tarihi': forms.DateInput(format=('%Y-%m-%d'), 
                                    attrs={'class':'myDateClass', 
                                    'placeholder':'Select a date' ,
                                    'type' : 'date'}) ,  
                                                                  
        }




class MulakatForm(forms.ModelForm):
    
    class Meta:
        model = Mulakat    
        fields = [
            'devam',
            'caba_calisma',
            'isi_vaktinde_yapma',
            'davranis',
            'arkadaslara_davranis',
            'proje',
            'duzen',
            'sunum',
            'icerik',
            'mulakat_degerlendirmesi',
        ]
        widgets = {
            'mulakat_tarhi': forms.DateInput(format=('%Y-%m-%d'), 
                                             attrs={'class':'myDateClass', 
                                            'placeholder':'Select date' ,
                                            'type' : 'date'}) , 
            'mulakat_saati': forms.TimeInput( 
                                    attrs={'class':'myTimeClass', 
                                'placeholder':'Select time' ,
                                'type' : 'time'}) , 
                                            
        }


class KonuForm(forms.ModelForm):
    
    class Meta:
        model = Konular
    
        fields = [
            'baslik' , 
        ]

class KomisyonForm(forms.ModelForm):
    
    class Meta:
        model = Komisyon

        fields = [
            'uye1_isim',
            'uye1_soyisim',
            'uye2_isim',
            'uye2_soyisim',
        ]


class GorusmeForm(forms.ModelForm):

    class Meta:
        model = Gorusme
        fields = [
            'gorusme_tarihi',
            'gorusme_saati',
            'komisyon',
        ]
        widgets = {
        'gorusme_tarihi': forms.DateInput(format=('%Y-%m-%d'), 
                                            attrs={'class':'myDateClass', 
                                        'placeholder':'Select date' ,
                                        'type' : 'date'}) , 
        'gorusme_saati': forms.TimeInput(   format=('%H:%M'),
                                            attrs={'class':'myTimeClass', 
                                            'placeholder':'Select time' ,
                                            'type' : 'time'}) , 
                                        
    }


class GunForm(forms.ModelForm):
    class Meta:
        model = Gun

        fields = [
            'toplam_gun',
        ]
    

        

