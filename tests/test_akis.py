"""
Tests – Hafta 4 Lab: Üreçler ve functools
==========================================
Tüm akis.py ve istatistik.py fonksiyonları için birim testler.
"""

import itertools
import functools
import pytest
from pathlib import Path

from uzay_oyunu.akis import (
    fibonacci,
    yakit_gostergesi,
    satirlari_oku,
    ayristir,
    uzun_yolculuklar,
    rota_sayaci,
)
from uzay_oyunu.istatistik import (
    buyuk_harfli_gezegenler_map,
    buyuk_harfli_gezegenler_liste,
    iki_baglantili_filter,
    iki_baglantili_liste,
    toplam_baglanti_reduce,
    toplam_baglanti_sum,
    yolculuk,
    hizli_yolculuk,
)

# ──────────────────────────────────────────────────
# Görev 1 – Fibonacci Üreteci Testleri
# ──────────────────────────────────────────────────

def test_fibonacci_ilk_uc():
    """next() ile ilk 3 değer doğru mu?"""
    g = fibonacci()
    assert next(g) == 0
    assert next(g) == 1
    assert next(g) == 1


def test_fibonacci_ilk_12():
    """islice ile ilk 12 değer doğru mu?"""
    sonuc = list(itertools.islice(fibonacci(), 12))
    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_100den_kucukler():
    """takewhile ile 100'den küçük Fibonacci sayıları doğru mu?"""
    sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    assert sonuc == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def test_fibonacci_tek_kullanimlik():
    """Üreç tek kullanımlıktır: ikinci islice çağrısı farklı sonuç verir."""
    g = fibonacci()
    ilk = list(itertools.islice(g, 5))    # [0, 1, 1, 2, 3]
    ikinci = list(itertools.islice(g, 5)) # [5, 8, 13, 21, 34]  – farklı!
    assert ilk != ikinci
    assert ilk == [0, 1, 1, 2, 3]
    assert ikinci == [5, 8, 13, 21, 34]


# ──────────────────────────────────────────────────
# Görev 2 – Yakıt Göstergesi Testleri
# ──────────────────────────────────────────────────

def test_yakit_gostergesi_basit():
    """100 yakıt, 30 tüketim → [70, 40, 10, 0]"""
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_gostergesi_tam_bolunur():
    """60 yakıt, 20 tüketim → [40, 20, 0]"""
    assert list(yakit_gostergesi(60, 20)) == [40, 20, 0]


def test_yakit_gostergesi_sifir_baslangic():
    """0 yakıt ile üreç hiç değer üretmemeli."""
    assert list(yakit_gostergesi(0, 10)) == []


def test_yakit_gostergesi_stopiteration():
    """Yakıt bitince StopIteration fırlatılır."""
    g = yakit_gostergesi(10, 10)
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


# ──────────────────────────────────────────────────
# Görev 3 – Boru Hattı Testleri
# ──────────────────────────────────────────────────

SEYIR_YOLU = str(Path(__file__).parent.parent / "veri" / "seyir.txt")


def test_satirlari_oku_yorum_atlar():
    """# ile başlayan satırlar atlanmalı."""
    satirlar = list(satirlari_oku(SEYIR_YOLU))
    for satir in satirlar:
        assert not satir.startswith("#")


def test_satirlari_oku_bos_atlar():
    """Boş satırlar atlanmalı."""
    satirlar = list(satirlari_oku(SEYIR_YOLU))
    for satir in satirlar:
        assert satir.strip() != ""


def test_ayristir_toplam_yakit():
    """Tüm kayıtların toplam yakıtı 88 olmalı."""
    toplam = sum(y for _, _, y in ayristir(satirlari_oku(SEYIR_YOLU)))
    assert toplam == 88


def test_ayristir_demetler():
    """ayristir doğru (kaynak, hedef, yakıt) demetleri üretmeli."""
    kayitlar = list(ayristir(satirlari_oku(SEYIR_YOLU)))
    assert kayitlar[0] == ("dünya", "sirius", 12)
    assert kayitlar[-1] == ("sirius", "kara_delik", 30)


def test_uzun_yolculuklar():
    """Eşiği (10) aşan yolculukların hedefleri doğru mu?"""
    kayitlar = ayristir(satirlari_oku(SEYIR_YOLU))
    uzun = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert uzun == ["sirius", "centauri", "orion", "kara_delik"]


def test_uzun_yolculuklar_boru_hatti_tembel():
    """Boru hattının tembel (lazy) çalıştığını doğrula – liste değil üreç döner."""
    kayitlar = ayristir(satirlari_oku(SEYIR_YOLU))
    uzun_gen = uzun_yolculuklar(kayitlar, 10)
    import types
    assert isinstance(uzun_gen, types.GeneratorType)


# ──────────────────────────────────────────────────
# Görev 4 – Önbellekli Rota Sayacı Testleri
# ──────────────────────────────────────────────────

ORNEK_BAGLANTILAR = {
    "dünya": ["centauri", "sirius", "orion"],
    "centauri": ["dünya", "sirius", "orion"],
    "sirius": ["dünya", "centauri", "orion", "kara_delik"],
    "orion": ["centauri", "sirius"],
    "kara_delik": ["sirius"],
}


def test_rota_sayaci_adim_0():
    """0 adımda her gezegenden tam 1 rota vardır (başlangıç noktası kendisi)."""
    say = rota_sayaci(ORNEK_BAGLANTILAR)
    assert say("dünya", 0) == 1
    assert say("kara_delik", 0) == 1


def test_rota_sayaci_adim_3():
    """Dünyadan 3 adımda 25 rota (bu galaksiye özgü değer)."""
    say = rota_sayaci(ORNEK_BAGLANTILAR)
    assert say("dünya", 3) == 25


def test_rota_sayaci_adim_10():
    """Dünyadan 10 adımda 37645 rota (bu galaksiye özgü değer)."""
    say = rota_sayaci(ORNEK_BAGLANTILAR)
    assert say("dünya", 10) == 37645


def test_rota_sayaci_cache_info():
    """lru_cache aktif ve en az bir cache hit oluşmuş olmalı."""
    say = rota_sayaci(ORNEK_BAGLANTILAR)
    say("dünya", 5)
    say("dünya", 5)  # ikinci çağrı önbellekten gelmeli
    bilgi = say.cache_info()
    assert bilgi.hits >= 1


# ──────────────────────────────────────────────────
# Görev 5 – map/filter/reduce ve partial Testleri
# ──────────────────────────────────────────────────

ORNEK_GALAKSI = {
    "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
    "baglantilar": {
        "dünya": ["centauri", "sirius", "orion"],
        "centauri": ["dünya", "sirius", "orion"],
        "sirius": ["dünya", "centauri", "orion", "kara_delik"],
        "orion": ["centauri", "sirius"],
        "kara_delik": ["sirius"],
    },
}


def test_buyuk_harfli_gezegenler_map():
    """map ile büyük harfli gezegen listesi doğru mu?"""
    beklenen = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELİK"]
    # Türkçe karakter farkını tolere etmek için her ikisi de upper() karşılaştırılır
    sonuc = buyuk_harfli_gezegenler_map(ORNEK_GALAKSI)
    assert [g.upper() for g in ORNEK_GALAKSI["gezegenler"]] == sonuc


def test_buyuk_harfli_gezegenler_liste():
    """Liste üreteci ile büyük harfli gezegen listesi doğru mu?"""
    sonuc = buyuk_harfli_gezegenler_liste(ORNEK_GALAKSI)
    assert sonuc == buyuk_harfli_gezegenler_map(ORNEK_GALAKSI)


def test_iki_baglantili_filter():
    """filter ile ≥2 bağlantılı gezegenler: kara_delik çıkmalı."""
    sonuc = iki_baglantili_filter(ORNEK_GALAKSI)
    assert "kara_delik" not in sonuc
    assert "dünya" in sonuc
    assert "sirius" in sonuc


def test_iki_baglantili_liste():
    """Liste üreteci ile filter aynı sonucu vermeli."""
    assert iki_baglantili_filter(ORNEK_GALAKSI) == iki_baglantili_liste(ORNEK_GALAKSI)


def test_toplam_baglanti_reduce():
    """reduce ile toplam bağlantı sayısı doğru mu?"""
    # dünya:3 + centauri:3 + sirius:4 + orion:2 + kara_delik:1 = 13
    assert toplam_baglanti_reduce(ORNEK_GALAKSI) == 13


def test_toplam_baglanti_sum():
    """sum ile toplam bağlantı sayısı reduce ile aynı olmalı."""
    assert toplam_baglanti_sum(ORNEK_GALAKSI) == toplam_baglanti_reduce(ORNEK_GALAKSI)


def test_hizli_yolculuk_partial():
    """hizli_yolculuk partial olarak hiz=3 sabit çalışmalı."""
    sonuc = hizli_yolculuk("sirius")
    assert "hız=3" in sonuc
    assert "sirius" in sonuc


def test_hizli_yolculuk_is_partial():
    """hizli_yolculuk bir functools.partial nesnesi olmalı."""
    assert isinstance(hizli_yolculuk, functools.partial)
