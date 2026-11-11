# SANAL DOST — Devir-Teslim Notu (v5.3 TAMAMLANDI → sonraki: v5.4)

> Bu dosya yeni bir sohbette projeye **az token harcayarak** devam etmek içindir.
> Önce bunu oku. Kod v5.3'ten beri **modüllere bölünmüş** (`dost/` klasörü, §1b haritası): sadece ilgili modülü aç.

## 0. Yeni sohbete ilk mesaj (kopyala-yapıştır)

```
Ekteki SanalDost_devir.zip içindeki DEVAM.md'yi oku ve oradaki "v5.3'te YAPILANLAR / sonraki fikirler" bölümünden devam et.
Dosyaları baştan sona okuma; §1b modül haritasını kullan. Değişiklikleri ilgili dost/*.py dosyasında (Edit ile) yap,
test_arac/ ile test et (python3 test11_akilli.py vb.), sonunda zip'i ver. Türkçe konuş, kısa yaz.
```

## 1. Proje nedir
Windows masaüstünde gezen **Türkçe tkinter sanal evcil dost** ("Sanal Dost"). Şeffaf (`-transparentcolor magenta`), çerçevesiz, hep üstte bir pencere; içinde Canvas ile çizilen sevimli yaratık. Tek dosya (`sanal_dost.py`), PyInstaller ile tek `.exe` yapılıyor (`derle.bat`).
Bağımlılıklar: `pystray`, `Pillow`, `psutil` (opsiyonel hepsi). Python 3.13, sadece standart kütüphane + bunlar.

Dosyalar:
- `sanal_dost.py` — giriş noktası (docstring, tek örnek kilidi, `main`) + `dost/` modüllerini birleştirir
- `dost/` — uygulamanın asıl kodu (§1b)
- `sanal_dost.ico`, `derle.bat` — exe yapımı
- `test_arac/` — sahte tkinter + sanal saat ile **Linux'ta** test/render aracı (bkz. §6)

## 1b. Modül haritası (v5.3)
`SanalDost` sınıfı `dost/uygulama.py`'de; metotları mixin'lerden gelir. Modüller arası `from dost.x import ad` kullanılır.
| Modül | İçerik |
|---|---|
| `ayar.py` | sabitler (W,H,ZEMIN…), `VARSAYILAN_AYARLAR`, TEMALAR, `YARDIM_METNI`, SURUM |
| `yardimci.py` | norm, clamp, hafıza dosyası, hata_kaydet, zaman, sistem bilgisi |
| `beyin.py` | Beyin (ihtiyaç, duygu, XP, rozet) |
| `anahtar.py` | API anahtarı saklama (DPAPI / obf) |
| `ai.py` | sağlayıcılar, `api_sor`, `ARACLAR` (AI araç tanımları, `dost_komutu` dahil) |
| `web.py` | hava, YouTube, site/arama |
| `sistem.py` | ekran görüntüsü, `monitorleri_al`, yerel OCR, geçmiş, dosya arama, `yazi_haritasi`, `ekran_yorumu_uret`, `tikla_gecir`, IZINLER |
| `fizik.py` | Yay |
| `hareket.py` | `_dongu`, durum makinesi, yürüme, `_yeni_hedef_sec` |
| `etkilesim.py` | fare, sürükleme, top modu, sağ tık menüsü |
| `zeka.py` | `_yavas`, `_dakikalik`, konuşma, balon |
| `cizim.py` | yaylar, yüz, `_ciz`, parçacıklar |
| `komutlar.py` | sohbet kutusu, komut tablosu, günlük özet |
| `izin.py` / `yapayzeka.py` / `araclar.py` / `oyun.py` / `panel.py` | izinler / AI sohbeti+araç eylemleri / hava,OCR,dosya / saklambaç,odak,Ctrl-çek / paneller |
| `gozlem.py` | **v5.3** yazı yoğunluğu haritası, okunan yerden kaçınma, ekran yorumu, özetle/çevir/hatayı çöz |
| `lazer.py` | **v5.3** lazer modu, `git <konum>` |
| `ayarlar_ui.py` | **v5.3** sekmeli Ayarlar penceresi (Anahtar düğmesi) |
Test ipucu: `sanal_dost.X = ...` ataması tüm `dost.*` modüllerine yayılır (monkeypatch uyumu).

## 1c. v5.3'te YAPILANLAR
- Kod 21 modüle bölündü; testler aynen geçiyor.
- ÇOKLU MONİTÖR: `monitorleri_al` (EnumDisplayMonitors), her monitörün kendi zemini, 5 sn'de bir yeniden algılama, ayarlar: `tum_monitorler`, `zemin` (görev çubuğu / ekran altı). Seçim/OCR/AI imlecin monitörünü kullanır.
- EKRAN FARKINDALIĞI: yazı yoğunluğu haritası (OCR yok, kenar şiddeti), hedef seçiminde okunan yer ve imleç cezası, yazı üstünde bekleyen dost çekilir (elle bırakılan yer 90 sn korunur). Ekran yorumu (kural tabanlı + isteğe bağlı AI, yalnız yazı gider, şifre/kart ekranına bakmaz).
- KOMUTLAR: yorumla, özetle, çevir, açıkla, hatayı çöz, cevap yaz, lazer, git <konum>, günlük özet, yazıdan kaçın, yorum modu.
- AI `dost_komutu` aracı: yapay zekâ tüm yerleşik komutları kullanabilir (YASAK_KOMUT listesi hariç: unut, izin, tam erişim, kustur…).
- Sağlık hatırlatıcıları: göz (20 dk), duruş (45 dk); sabah özeti.
- Ayarlar baştan: Ana sayfa (hızlı eylemler), Davranış, Ekran ve akıl, Yardımcılar, İzinler, Komutlar, Hakkında.
- Windows'ta TEST EDİLMEMİŞ (burada yalnız Linux+sahte tkinter): EnumDisplayMonitors, ImageGrab all_screens, tikla_gecir (lazer noktası), sekmeli Ayarlar'ın gerçek Tk görünümü, çoklu monitörde Ctrl-çek.

## 1d. v5.4 fikir havuzu
Antialiasing + UpdateLayeredWindow, kıyafet/aksesuar, yumak/oyuncak, pencere kenarına oturma, ses efektleri, balon yenileme, günlük istatistik grafiği, hafıza yedeği, EN arayüz.

## 2. Mimari (kısa)
- **Pencere**: W,H = 230×215; ZEMIN=198 (zemin çizgisi), CY0=156 (gövde merkezi), GOLGE_Y=201, BAL_ALT=100 (balon), KUTU_Y=124 (sohbet kutusu).
- **Döngüler**: `_dongu` (40 ms, fizik+çizim) · `_yavas` (1 sn; hava, YouTube, hatırlatıcı, ihtiyaçlar) · `_sinyal_kontrol` (200 ms; `self.kuyruk` kuyruğu: tray olayları ve `("sonuc", cb, sonuc)` ile arka plan iş parçacığı sonuçları).
- **Durum makinesi**: `self.durum` ∈ BEKLE, YURU, OTUR, UYU, SEKERLEME, YEMEK, SURUKLE, ZIPLA, DANS, GERIN, DUSUN, KACIS, SAKLAN_GIT, SAKLI, ALARM, VUR_GIT, VUR. Geçiş: `_durum_gec(ad, sure)`. Özel durumlarda (SURUKLE/SAKLI/SAKLAN_GIT/VUR/VUR_GIT/ALARM) `_zipla` ve `_k_hareket/_k_uyu` kendini reddeder.
- **Çizim**: `_ciz` her karede "dost" etiketli canvas öğelerini silip yeniden çizer; balon "bal" etiketli. Gövde uzayında `X(dx,dy)`, `Y(dy)` yardımcıları + squash ölçeği `sx,sy`. Yardımcılar: `_o` (oval), `_pol`, `_ln`, `_arc`.
- **Beyin** (`class Beyin`): ihtiyaçlar (enerji/tokluk/ilgi/eğlence), kişilik, ruh hali, XP/seviye/aşama, `eylem_sec` (ağırlıklı rastgele), rozetler.
- **Hafıza**: Masaüstündeki JSON (`HAFIZA_DOSYASI`), atomik kayıt; ayarlar `hafiza["ayarlar"]` (varsayılanlar `VARSAYILAN_AYARLAR`, satır ~98). API anahtarı **ayrı** dosyada: `~/.sanal_dost_gizli.json`.
- **Komutlar**: `norm()` (Türkçe katlama, uzunluk korur) + regex tablosu `_komut_tablosu_kur` (ilk eşleşen kazanır; işleyici `str` ya da `None` döner → `None` ise sonrakine düşer). `_g()` orijinal metinden grup çeker. Sıra: onay → dost adı soyma → oyun → öğrenilmiş cevap → tablo → hesap → (AI hazırsa) AI.
- **Onay sistemi**: `_onay_iste(metin, evet_fonksiyonu)` / `_onay_cevabi`. Tarayıcıyı etkileyen AI eylemleri hep onay ister.
- **Ağ**: `http_al` (urllib), Open-Meteo (anahtarsız), YouTube RSS (regex), Anthropic Messages API (`api_sor`, araçlar: url_ac, youtube_ara, web_ara, uygulama_ac, hatirlat, not_al, odak_baslat). Arka plan: `_arka(fonksiyon, cb)` → sonuç kuyruğa gider.

## 3. Kod haritası (v5.1'e göre; satırlar kaydı, güncel harita §7'de; kaydıkça `grep -n "def _xxx"` kullan)
| Satır | Bölüm |
|---|---|
| 77–116 | SURUM, VARSAYILAN_AYARLAR, TEMALAR (6 renk, seviyeyle açılır), AŞAMALAR, XP eşikleri |
| 117–195 | Metin havuzları (SELAM vb.) |
| 198–270 | `norm, tr_baslik, clamp, karistir, gece_mi, sure_metni, guvenli_hesap` |
| 276–360 | Dosya yolları (`masaustu_klasorunu_bul`, `kaynak_yolu`, `hata_kaydet`), hafıza yükle/kaydet |
| 360–500 | Sistem: boşta kalma, tam ekran, çalışma alanı, otomatik başlat, sistem bilgisi |
| 500–688 | `ETKILER`, `ROZETLER`, **`class Beyin`** |
| 689–962 | Ağ yardımcıları: `http_al`, **API anahtarı (722–750)**, hava (752), YouTube (805), siteler/`guvenli_url` (837), ekran görüntüsü/pano (863), **Claude API `api_sor` (918–960)** |
| 966 | **`class SanalDost`** başlangıcı; `__init__` 967–1118 |
| 1119–1215 | Küçük yardımcılar (`ayar`, `tema`, `_xp`, `_duygu`, `_acilis_mesaji`) |
| 1216–1454 | `_dongu`, `_fizik`, `_durum_isle`, `_hiz`, `_yuru`, `_varildi`, `_zipla`, `_besle`, `_yemek_bitti` |
| 1455–1660 | Fare: `_bas/_surukle/_birak/_tek_tik_isle`, `_menu_ac` (sağ tık menüsü), `_fare_kontrol`, `_yakalandi` |
| 1657–1875 | `_yavas`, `_bosta_kontrol`, düşünce/sohbet üreticileri |
| 1876–1967 | `konus`, balon çizimi, parçacık sistemi |
| 1968–2290 | **Çizim**: `_ifade`, `_poz`, `_ciz`, `_gozler`, `_agiz_ciz`, `_yem_ciz`, `_parcaciklari_ciz` |
| 2291–2475 | Sohbet kutusu, **komut tablosu**, `_komut_isle` |
| 2476–2857 | Klasik komutlar (`_k_*`: not, yapılacak, hatırlat, zar, oyunlar…) |
| 2858–3171 | `_arka`, `_ses`, dost adı, onay, `_url_ac`, `_k_ara/_k_ac`, **AI (`_ai_hazir/_ai_sor/_ai_eylem`)**, **`_ayarlar_penceresi` (3090)** |
| 3172–3312 | Hava durumu, YouTube kanal takibi |
| 3313–3553 | Yutma (alan seç → `_secim_*`, `_karina_ekle`, `_kustur`, `_k_oku`), Saklambaç |
| 3554–3706 | **Odak/pomodoro**, alarm titremesi, sıkı odak `VUR`, `_saat_ciz`, `_vur_ciz` |
| 3707–3910 | Paneller (notlar, durum kartı), tray, `_sinyal_kontrol`, `kapat`, `main` |

## 4. Şu an çalışan özellikler (v5.1)
Seviye/aşama/tema sistemi, ihtiyaçlar, kişilik, rozetler, gün serisi, notlar/yapılacaklar/hatırlatıcılar, öğretme, oyunlar (yakalamaca, tkm, tahmin, **saklambaç**), hesap makinesi, hava (çevrimdışıyken sessiz), YouTube favori kanal takibi + "yeni video var, açayım mı?", alan seç → dost tıklanınca **yut/kustur** (pano; yapıştırma = `kustur` sonrası kullanıcı Ctrl+V), **sıkı odak** (fare oynarsa 5 darbe), odak sırasında **iki elle saat tutma**, bitince alarm titremesi (fare oynayana kadar), sağ tık **Ayarlar** (dost adı, API anahtarı, model, kısayollar…), asistan: "youtube'da X ara", "şunu aç", AI araç çağrıları, "ekrana bak".

## 5. Bilinen kararlar / tuzaklar
- Yapıştırma otomatik tuş basmaz: panoya koyar, kullanıcı Ctrl+V yapar.
- Karın (yutulanlar) sadece bellekte.
- "İmleçe vur" sadece animasyon; imleç gerçekten itilmez.
- YouTube "en çok baktığın kanal" şimdilik sadece dostun açtığı kanalları sayar.
- `SURUM` sabiti "5.2".
- **Windows'a özel ve gerçek Windows'ta HİÇ test edilmemiş**: DPAPI (henüz yok), `SHGetFolderPath`, CF_DIB pano, `winsound`, `os.startfile`, `SetCursorPos`, `GetAsyncKeyState`, PowerShell OCR, otomatik başlat kayıt defteri. Kullanıcı hata bildirirse `~/Desktop` altındaki hata günlüğüne (`HATA_DOSYASI`) bakılacak.
- Değişiklikten sonra mutlaka: `python3 -m py_compile sanal_dost.py` + `test_arac` testleri.

## 6. Test aracı (`test_arac/`)
Gerçek tkinter olmadığından sahte `tkinter` (stub/) + sanal saat var.
```
cd test_arac
python3 test1.py          # komutlar        python3 test4.py   # odak/alarm/vur
python3 test2.py          # hafıza/kayıt    python3 test4b.py  # yutma/saklambaç
python3 test3.py          # hareket         python3 test6.py   # hava çevrimdışı
python3 gallery.py        # PNG galeri (Pillow ile render) -> galeri_*.png
```
`harness.py`: `run(sn)` sanal zamanı ilerletir, `HATALAR` listesi `hata_kaydet`'i yakalar. Gerçek iş parçacığı testlerinde `time.sleep(0.3)` sonra `run(1)`. Görsel doğrulama için `render.py` canvas çağrılarını PIL'e çizer (galeriyi `Read` ile görüntüle). Hepsi şu an HATALAR=0.

## 7. v5.2'de YAPILANLAR (hepsi tek dosyada: sanal_dost.py)
Kod haritası (yaklaşık; `grep -n "def _xxx"` kullan):
- **Animasyon**: `class Yay`, `YAY_AYAR`, `_olaylar` (durum/duygu değişince yaylara tekme), `_poz` (hedef poz), `_yaylar`, `_yuz_hedef/_yuz_isle` (lerp), `_ciz`, `_gozler`, `_kaslar`, `_agiz_ciz`, `_emote/_emote_ciz`, `_fidget_isle` (boşta hareketler), `_toz`. Zıplama artık çömelir (`firla_at`).
- **Top modu** (`top_modu` ayarı, sağ tık menüsü, `top modu aç/kapat`): `_surukle_izle` (sallama = yön değiştirme sayısı), `_birakma_hizi`, `_firlat_baslat/_firla_isle` (yerçekimi 2200, duvar sekmesi 0.82, zemin 0.70, alt-adım entegrasyonu), `_firla_carpma`, `_sersem_ver/_sersem_isle` (sarmal göz + dönen yıldız + kafa dairesi). Durumlar: `FIRLA`, `SERSEM`.
- **İzinler**: `IZINLER` sözlüğü, `izin(ad)`, `_izin_iste` (evet=45 sn geçici, hep=kalıcı), `tam_erisim` (sadece listedekileri açar; dosya silme/tuş basma/komut çalıştırma YOK). Ayarlar penceresi kaydırmalı, yeniden yazıldı (`_ayarlar_penceresi`).
- **Anahtar/sağlayıcı**: `sifrele/coz` (DPAPI, Windows dışı "obf:" sadece gizleme), `gizli_yukle` (v1→v2 taşıma), `SAGLAYICILAR`, `guvenli_base`, `api_sor(cfg, sistem, mesajlar, araclar=…)` (Anthropic + OpenAI uyumlu, araç/görsel dönüşümü, 400+tools'ta araçsız yeniden dene), `ai_dene`, `_ai_cfg`.
- **Yerel**: `yerel_ocr` (Windows WinRT PowerShell → Tesseract yedek), `_resmi_oku/_k_ekran_oku/_k_ekranda_var`, `gecmisten_youtube/favori_kanallar_gecmisten/_k_gecmis_kanal`, `dosya_bul/_k_dosya_bul/_k_dosya_goster`.
- **Ctrl-çek**: `tus_basili`, `imleci_koy`, `_ctrl_kontrol` (2 sn'de 6 Ctrl), `_cek_baslat/_cek_isle/_cek_bitir/_cek_ciz`; durumlar `CEK_GIT`, `CEK`. İptal: Esc, sol tık, kullanıcı fareyi 30 px'ten fazla oynatırsa, 10 sn.

Test araçları (`test_arac/`): test1–6 eski; **test7_top.py** (top modu simülasyonu), **test8_izin.py** (anahtar, sağlayıcı, izin akışı, OCR, geçmiş, dosya arama, Ctrl-çek, Ayarlar), **gallery.py / gallery2.py / gallery3.py** (PNG kareleri: durumlar, top/sersem). Çalıştır: `cd test_arac && python3 testN.py` (stub tkinter, sanal zaman). Testler izin kapılarını kullanır: örn. `d.hafiza["ayarlar"]["izinler"]["ekran_yerel"]=True`.

### Windows'ta HİÇ test edilmedi (bildirim gelirse HATA_DOSYASI'na bak)
DPAPI (`_dpapi`), PowerShell OCR betiği (`OCR_PS`), `GetAsyncKeyState`, `SetCursorPos`, Chrome/Edge geçmiş yolları, explorer `/select`. Hepsi try/except ile sessiz düşer; OCR Windows'ta çalışmazsa Tesseract yedeği, o da yoksa kullanıcıya açık mesaj verir.

### Bilinçli sınırlar
- Tam erişim = yalnızca IZINLER listesi. Genel kabuk/dosya silme/tuş enjeksiyonu EKLENMEDİ ve eklenmemeli.
- Dosya aramada dosya AÇILMAZ (çalıştırma riski), yalnızca klasörü gösterilir.
- Ekran görüntüsü yapay zekâya sadece `ekran_ai` izniyle gider; yerel OCR hiçbir yere göndermez.
- Top modunda pencere gövde merkezine göre sınırlanır (`_firla_sinirlar`); çok çözünürlüklü ekranlarda yalnızca ana ekran alanı.

## 8. Öneri havuzu (sunulmadı/yapılmadı)
Top modunda: dostu ekran kenarına fırlatınca duvarda asılı kalma, hız çizgileri, ses efekti; fidget'a "yazı yazan kullanıcıya bakma"; emote setine nota/ampul; Saklambaçta dostun **seni araması**; panoda arama; günlük özet ("bugün ne yaptık"); su içme animasyonu; hava durumuna göre kıyafet/şemsiye; uygulama bazlı odak beyaz listesi; ses/ses efektleri; otomatik güncelleme; hafıza yedeği + içe/dışa aktar; çoklu dil (EN); mini oyunlar (balon patlat, yakalamaca skor tablosu); takvim/ICS hatırlatıcı içe aktarma; Pomodoro istatistik grafiği; ekran kenarlarında tırmanma/ekran altında uyuma pozisyonları.

## 9. Kullanıcı bilgileri
Kullanıcı Türkçe konuşuyor, çoğunlukla kısa/konuşma dilinde ister; çok özellik ve "başka öneriler" sunulmasını seviyor. Kredi/token tasarrufu önemsiyor: tüm dosyayı yeniden yazma, **hedefli Edit** yap, uzun anlatım yapma.
