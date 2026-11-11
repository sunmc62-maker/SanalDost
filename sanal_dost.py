#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanal Dost v5 - Tanıyan, Düşünen, Konuşan, Kaçan, Hafızalı Yaratık
--------------------------------------------------------------------
Tamamen GÜVENLİ bir masaüstü arkadaşı. Gerçekte:
  - Hiçbir dosyanın İÇERİĞİNE dokunmaz, hiçbir şeyi silmez
  - Hiçbir programı/pencere başlığını algılamaya çalışmaz, yazdıklarını görmez
    (sadece SEN izin verirsen: 'Ctrl basılı mı' bilgisine bakar, bkz. Ayarlar > İzinler)
  - Okuduğu TEK şeyler: genel sistem durumu (CPU/RAM/disk/pil/açık kalma),
    fare imlecinin konumu, "ne kadar süredir dokunulmadı" bilgisi ve
    (Windows'ta) tam ekran uygulama var mı bilgisi
  - Hafızasını şu dosyada tutar: Masaüstü/sanal_dost_hafiza.json
    (silersen hafızası sıfırlanır; v4 hafızası otomatik devralınır)

V5 YENİLİKLERİ
--------------
* AKIL: dört ihtiyacı (enerji, tokluk, ilgi, eğlence), gelişen bir kişiliği
  (sosyal, oyuncu, tembel, meraklı), ruh hali ve bağ seviyesi var.
  Ne yapacağına bu değerlerle, saatle ve senin hareketsizliğinle karar verir.
* TASARIM: göz imleci takip eder, gerçek yüz ifadeleri, gölge, nefes,
  sıkışıp uzama, parçacıklar (kalp, zzz, yıldız, konfeti), 6 renk teması,
  büyüdükçe atkı ve taç, gece uyku külahı, odak modunda gözlük.
* ETKİLEŞİM: sürükle-bırak, tek tık sevme, çift tık sohbet, sağ tık menüsü.
* SOHBET: Türkçe anlayan komutlar, öğretilebilir cevaplar, not, yapılacaklar,
  hatırlatıcı, hesap makinesi, 4 oyun (zar, yazı-tura, taş-kağıt-makas, tahmin).
* PRODUKTİVİTE: pomodoro odak modu, mola ve su hatırlatıcısı.
* Sistem tepsisi, tek örnek koruması, Windows ile başlat (menüden isteğe bağlı).

V5.1 (isteğe bağlı, hepsi Ayarlar'dan açılıp kapatılır)
* Saklambaç, hava durumu (internet yoksa otomatik yorumlar sessiz kalır),
  YouTube kanal takibi ("kanal ekle @kanal"), "youtube'ta lofi ara", "aç gmail".
* Alan seç > dosta tıkla > yutar ve panoya kopyalar; "kustur" ile geri verir.
* Odak: iki elle saat tutar, süre bitince fare oynayana kadar titrer.
  Sıkı odak: fare oynarsa imlece 5 kez vurur (sadece animasyon).
* Sağ tık > Ayarlar: dostun adı, şehir, kısayollar, Claude API anahtarı
  (anahtar Masaüstü dosyasından AYRI, kullanıcı klasöründe saklanır).
  Anahtar girersen: serbest sohbet, "ekrana bak" (görüntü Claude'a gönderilir,
  sadece sen isteyince ve izin verirsen), yazıyı oku. Tarayıcı açma önerileri onay ister.

V5.3
* Kod artık dost/ klasöründe modüllere bölünmüş (bu dosya giriş noktası).
* ÇOKLU MONİTÖR: tüm ekranlarda gezer; zemin: görev çubuğu üstü ya da ekranın en altı (Ayarlar).
* AKILLI EKRAN: okuduğun yazının ve imlecin üstüne basmaz; yorumla / özetle / çevir / hatayı çöz / cevap yaz.
* LAZER MODU ('lazer'): imleci lazer noktası gibi kovalar. 'git sağ üst', 'günlük özet'.
* Yapay zekâ dostun tüm komutlarını kullanabilir; göz ve duruş hatırlatıcıları; yeni sekmeli Ayarlar.

V5.2
* ANİMASYON: yaylı (spring) fizik, zıplamadan önce çömelme, kafa dönüşü, parametrik yüz
  (kedi ağzı, iri parlak gözler, kaş, yanak), kulak/kuyruk/kol yayları, boşta esneme/kaşınma/
  silkinme/kulak seğirtme, uyurken sümük balonu, yürürken ve inişte toz, duygu simgeleri.
* TOP MODU (Ayarlar'dan açılır): dostu tut, salla, bırak -> ekran kenarlarına çarparak seker.
  Çok sallarsan başı döner (sarmal gözler, dönen yıldızlar).
* İZİNLER: Ayarlar > İzinler listesi (hassas olanlar kapalı; kapalıyken dost evet/hayır/hep diye sorar).
  İsteğe bağlı TAM ERİŞİM: yalnızca o listedekilerin hepsini birden açar.
* API anahtarı: Windows DPAPI ile şifreli, sağlayıcı seç (Anthropic, OpenAI, Gemini, Groq, OpenRouter,
  DeepSeek, Mistral, Ollama, özel). "ekranı oku" yapay zekâsız (yerel OCR). Tarayıcı geçmişinden favori
  YouTube kanalları. "dosya bul <ad>". Ctrl'ye art arda basınca imleci ekran ortasına çeker.

Çalıştırmak için:   python sanal_dost.py
Kapatmak için:      sağ tık > Kapat / tepsi ikonu > Çıkış / Ctrl+C
Komutları görmek için: çift tıkla, "yardım" yaz.
"""

import signal
import socket
import sys
import types

from dost import kutuphane, ayar, yardimci, beyin, anahtar, ai, web, sistem, fizik, hareket, etkilesim, zeka, cizim, komutlar, izin, yapayzeka, ayarlar_ui, araclar, oyun, panel, gozlem, lazer, uygulama
from dost.ayar import SURUM, TEK_ORNEK_PORT
from dost.kutuphane import SYSTRAY_MEVCUT
from dost.uygulama import SanalDost
from dost.yardimci import HAFIZA_DOSYASI

_MODULLER = [kutuphane, ayar, yardimci, beyin, anahtar, ai, web, sistem, fizik, hareket, etkilesim, zeka, cizim, komutlar, izin, yapayzeka, ayarlar_ui, araclar, oyun, panel, gozlem, lazer, uygulama]

# Eski tek dosyalı sürümle uyum: sanal_dost.ADI ile her şeye ulaşılır, test/araçlar
# sanal_dost.ADI = ... dediğinde değer ilgili modüllere de işlenir.
for _m in _MODULLER:
    for _k, _v in vars(_m).items():
        if not _k.startswith("__"):
            globals().setdefault(_k, _v)


class _Modul(types.ModuleType):
    def __setattr__(self, ad, deger):
        types.ModuleType.__setattr__(self, ad, deger)
        for _mod in _MODULLER:
            if ad in vars(_mod):
                setattr(_mod, ad, deger)


sys.modules[__name__].__class__ = _Modul


def tek_ornek_kilidi():
    """Aynı anda iki Sanal Dost açılmasını engeller (yerel port kilidi)."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("127.0.0.1", TEK_ORNEK_PORT))
        return s
    except OSError:
        return None
    except Exception:
        return True


def _ctrl_c_yakala(dost):
    signal.signal(signal.SIGINT, lambda signum, frame: dost.kapat())


if __name__ == "__main__":
    kilit = tek_ornek_kilidi()
    if kilit is None:
        print("Sanal Dost zaten çalışıyor.")
        sys.exit(0)
    dost = SanalDost()
    _ctrl_c_yakala(dost)
    print(f"Sanal Dost v{SURUM} ekranda. Çift tık: sohbet | Tek tık: sev | Sürükle: taşı | Sağ tık: menü")
    print(f"Hafıza dosyası: {HAFIZA_DOSYASI}")
    if not SYSTRAY_MEVCUT:
        print("(Sistem tepsisi için: pip install pystray Pillow)")
    dost.calistir()
