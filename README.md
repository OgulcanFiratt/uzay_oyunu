# İleri Python Programlama – Hafta 3 & 4 Lab Ödevi

**Öğrenci:** Oğulcan Fırat  
**Numara:** 20253004003  
**Ödev:** İleri Python Programlama  
**Dönem:** 2026–2027 Güz  

---

## Hafta 3 – Proje Dosyaları ve Görevler

- `uzay_oyunu/oyun.py`: 
  - **Görev 1:** Saf fonksiyonlar (`envanter_metni`, `hedef_menusu`).
  - **Görev 3:** Galaksi kurulumu (`galaksi_kur`, `galaksiyi_yukle`) ve `travel()` ana oyun döngüsü.
- `uzay_oyunu/kayit.py`: 
  - **Görev 2:** `*args`, `**kwargs` ve keyword-only parametreli `gorev_kaydi()`.
- `uzay_oyunu/galaksi.json`: 
  - **Görev 3:** Galaksi haritası, gezegenler ve bağlantı verileri.
- `kapsam.md`: 
  - **Görev 4:** LEGB kuralı, kapsam tahminleri, `UnboundLocalError` ve mutable varsayılan argüman tuzağının analizi.
- `uzay_oyunu/araclar.py`: 
  - **Görev 5:** Closure ile `hamle_sayaci` (`nonlocal`), lambda ile `en_bagli_gezegenler`.
- `tests/test_fonksiyonlar.py`: Görev 1, 3 ve 5 için birim testler.
- `tests/test_tuzaklar.py`: Görev 4 için mutable argüman ve kapsam testleri.

---

## Hafta 4 – Üreçler ve functools

### Yeni Dosyalar

- `uzay_oyunu/akis.py`:
  - **Görev 1:** `fibonacci()` — Sonsuz Fibonacci üreteci. `next()`, `itertools.islice` ve `itertools.takewhile` ile kullanım gösterimi.
  - **Görev 2:** `yakit_gostergesi(yakit, tuketim)` — Her seyahatte yakıt azaltan üreç; bitince `StopIteration`.
  - **Görev 3:** `satirlari_oku()`, `ayristir()`, `uzun_yolculuklar()` — Üç aşamalı tembel boru hattı.
  - **Görev 4:** `rota_sayaci(baglantilar)` — `@lru_cache` ile önbellekli iç fonksiyon döner.
  - **Bonus:** `zamanlayici(aralik)` — Meşgul bekleme tabanlı zamanlayıcı üreteci.
- `uzay_oyunu/istatistik.py`:
  - **Görev 5:** `map`, `filter`, `functools.reduce` ile liste üreteci/`sum` karşılaştırması; `functools.partial` ile `hizli_yolculuk` türetimi.
- `veri/seyir.txt`: Görev 3 boru hattının okuduğu seyir defteri verisi.
- `tests/test_akis.py`: Hafta 4 görevlerinin tüm birim testleri (26 test).

---

## Görev 4 – Önbellek Performans Ölçümü

`rota_sayaci` içindeki `@lru_cache` etkisi `time.perf_counter()` ile ölçüldü (adim=15, "dünya" başlangıcı):

| Yöntem | Süre | Sonuç |
|---|---|---|
| Önbelleksiz özyineleme | **2.3896 sn** | 6 960 671 |
| `@lru_cache` ile | **0.000094 sn** | 6 960 671 |

**Hız oranı: ~25 000×**

```
CacheInfo(hits=108, misses=74, maxsize=None, currsize=74)
```

Önbellekli sürüm adim=20 için ise **0.000026 sn** içinde yanıt verir (sonuç: 1 287 228 073).

---

## Testleri Çalıştırma

Tüm testleri çalıştırmak için terminalde:
```bash
uv run pytest
```
veya
```bash
pytest
```

---

## Oyunu ve Modülleri Çalıştırma

Uzay oyununu başlatmak için:
```bash
uv run python -m uzay_oyunu.oyun
```

Görev 2 (Kayıt) modülünü denemek için:
```bash
uv run python -m uzay_oyunu.kayit
```

Görev 5 (Araçlar) modülünü denemek için:
```bash
uv run python -m uzay_oyunu.araclar
```

Hafta 4 – Akış modülünü denemek için:
```bash
uv run python -m uzay_oyunu.akis
```

Hafta 4 – İstatistik modülünü denemek için:
```bash
uv run python -m uzay_oyunu.istatistik
```
