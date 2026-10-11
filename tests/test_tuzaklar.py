import pytest


# (a) Hatalı fonksiyon (varsayılan liste bir kez oluşturulur ve tüm çağrılarda paylaşılır)
def yakit_ekle_hatali(miktar: int, depo: list = []):
    depo.append(miktar)
    return depo


# (a) Düzeltilmiş fonksiyon (None kalıbı ile her çağrıda yeni liste oluşturulur)
def yakit_ekle(miktar: int, depo: list | None = None) -> list:
    """Belirtilen depoya veya yeni bir depoya yakıt ekler."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_yakit_ekle_hatali_davranisi():
    """Hatalı fonksiyonda önceki çağrının depoyu kirlettiğini gösteren test."""
    yakit_ekle_hatali.__defaults__[0].clear()
    ilk = yakit_ekle_hatali(10)
    assert ilk == [10]

    ikinci = yakit_ekle_hatali(20)
    # Burada liste sıfırlanmadı, 10'un üstüne 20 eklendi:
    assert ikinci == [10, 20]


def test_yakit_ekle_duzeltilmis():
    """Düzeltilmiş fonksiyonda her çağrının bağımsız yeni bir liste ürettiğini doğrular."""
    sonuc1 = yakit_ekle(10)
    assert sonuc1 == [10]

    sonuc2 = yakit_ekle(20)
    assert sonuc2 == [20]


def test_yakit_ekle_harici_depo():
    """Kullanıcı kendi listesini verirse o listeye ekleme yapıldığını doğrular."""
    ozel_depo = [5, 15]
    sonuc = yakit_ekle(25, ozel_depo)
    assert sonuc == [5, 15, 25]


# (b) Kapsam (Scope) Testleri
global_degisken = "galaksi"


def test_kapsam_1_global_okuma():
    """Fonksiyon içinden global değişkenin başarıyla okunması."""
    def oku():
        return f"Konum: {global_degisken}"

    assert oku() == "Konum: galaksi"


def test_kapsam_2_yerel_golgeleme():
    """Yerel değişkenin global değişkeni gölgelemesi (shadowing)."""
    def golgele():
        global_degisken = "mars"
        return global_degisken

    assert golgele() == "mars"
    # Dışarıdaki global değişkenin değişmediğini doğrularız:
    assert global_degisken == "galaksi"


def test_kapsam_3_unbound_local_error():
    """Atama yapılmadan önce okunan yerel değişkenin UnboundLocalError fırlatması."""
    sayi = 100

    def hatali():
        gecici = sayi  # Alt satırda yerel atama olduğu için Python bunu yerel sayar ama henüz değeri atanmadı
        sayi = 200
        return gecici + sayi

    with pytest.raises(UnboundLocalError):
        hatali()
