# İleri Python Programlama – Hafta 3 Lab Ödevi

**Öğrenci:** Oğulcan Fırat  
**Numara:** 20253004003  
**Ödev:** İleri Python Programlama  
**Dönem:** 2026–2027 Güz  

---

## Proje Dosyaları ve Görevler

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
