from django.urls import path 
from . import views

app_name = 'staj'

urlpatterns = [
    
    #Öğrenci fonksiyonlarının yollarını burada veriyoruz
    path('', views.home),
    path('ogrenciler/', views.get_ogrenci),
    path('ogrenci_details/<int:pk>/', views.ogrenci_details , name ="detail"),
    path('ogrenci_ekle/', views.add_ogrenci , name ="ekle"),
    path('ogrenci_details/<int:pk>/duzenle/', views.ogrenci_edit , name ='edit'),
    path('ogrenci_details/<int:pk>/delete/', views.ogrenci_delete , name ='delete'),
    path('ogrenci_details/<int:pk>/dosya_ekle/', views.add_ogrenci_dosya , name ='dosya_ekle'),

    #Staj fonksiyonlarının yollarını burada veriyoruz
    
    path('stajlar/', views.get_staj ),
    path('staj_ekle/<int:pk>/', views.add_staj , name ="staj_ekle"),
    path('staj_details/<int:pk>/', views.staj_details , name ="staj_detay"),
    path('staj_details/<int:pk>/duzenle/', views.staj_edit , name ='staj_edit'),
    path('staj_details/<int:pk>/delete/', views.staj_delete , name ='staj_sil'),

    #Konu fonksiyonlarının yollarını burada veriyoruz
    
    path('konular/', views.get_konu ),
    path('konu_ekle/', views.konu_add  , name = 'konu_ekle'),
    path('konu_duzenle/<int:pk>/', views.konu_duzenle  , name = 'konu_duzenle'),
    path('konu_sil/<int:pk>/', views.konu_delete  , name = 'konu_sil'),
    
    #Mulakat fonksiyonlarının yollarını burada veriyoruz
    
    path('stajlar/mulakatlar/', views.get_mulakat ),
    path('stajlar/mulakat_ekle/<int:pk>/', views.mulakat_add  , name = 'mulakat_ekle'),
    path('stajlar/mulakat_details/<int:pk>/', views.mulakat_details , name ='mulakat_detay'),
    path('stajlar/mulakat_duzenle/<int:pk>/', views.mulakat_duzenle  , name = 'mulakat_duzenle'),
    path('stajlar/mulakat_sil/<int:pk>/', views.mulakat_delete  , name = 'mulakat_sil'),
    
    #pdf url atamaları
    path('pdf_mulakatlar/', views.get , name = 'mulakatlar_pdf_indir'),
    path('pdf_gorusmeler/', views.get_gorusme_pdf , name = 'gorusmeler_pdf_indir'),
    path('pdf_ogrenciler/', views.pdf_ogrenciler , name = 'ogrenciler_pdf_indir'),


    path('gorusmeler_exel/', views.gorusmeler_exel , name = 'gorusmeler_exel'),
    path('mulakatlar_exel/', views.mulakatlar_exel , name = 'mulakatlar_exel'),
    path('ogrenciler_exel/', views.ogrenciler_exel , name = 'ogrenciler_exel'),


    path('komisyonlar/', views.get_komisyon ),
    path('komisyon_ekle/', views.komisyon_add  , name = 'komisyon_ekle'),
    path('komisyon_duzenle/<int:pk>/', views.komisyon_duzenle  , name = 'komisyon_duzenle'),
    path('komisyon_sil/<int:pk>/', views.komisyon_delete  , name = 'komisyon_sil'),

    path('stajlar/gorusmeler', views.get_gorusme ),
    path('stajlar/gorusme_ekle/<int:pk>', views.gorusme_add  , name = 'gorusme_ekle'),
    path('stajlar/gorusme_duzenle/<int:pk>/', views.gorusme_duzenle  , name = 'gorusme_duzenle'),


    path('stajlar/gun_sayisi/<int:pk>/', views.gun_setle  , name = 'staj_gun'),



]


