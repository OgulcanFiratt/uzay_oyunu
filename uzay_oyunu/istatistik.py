import functools
import json
from pathlib import Path


def _galaksiyi_yukle() -> dict:
    #galaksi.json dosyasını yükler ve döner.
    yol = Path(__file__).parent / "galaksi.json"
    with open(yol, encoding="utf-8") as f:
        return json.load(f)


def buyuk_harfli_gezegenler_map(galaksi: dict) -> list[str]:
    #map() kullanarak gezegen adlarını büyük harfe çevirir.
    return list(map(str.upper, galaksi["gezegenler"]))


def buyuk_harfli_gezegenler_liste(galaksi: dict) -> list[str]:
    #Liste üreteci kullanarak gezegen adlarını büyük harfe çevirir.
    # Liste üreteci daha okunakl; hangi dönüşüm yapıldığı açıkça görünür.
    return [g.upper() for g in galaksi["gezegenler"]]


def iki_baglantili_filter(galaksi: dict) -> list[str]:
    #filter() kullanarak en az 2 bağlantısı olan gezegenleri döner.
    baglantilar = galaksi["baglantilar"]
    return list(
        filter(lambda g: len(baglantilar.get(g, [])) >= 2, galaksi["gezegenler"])
    )


def iki_baglantili_liste(galaksi: dict) -> list[str]:
    #Liste üreteci kullanarak en az 2 bağlantısı olan gezegenleri döner.
    baglantilar = galaksi["baglantilar"]
    return [g for g in galaksi["gezegenler"] if len(baglantilar.get(g, [])) >= 2]


def toplam_baglanti_reduce(galaksi: dict) -> int:
    #functools.reduce() kullanarak tüm bağlantıların toplam sayısını hesaplar.
    sayilar = list(map(len, galaksi["baglantilar"].values()))
    return functools.reduce(lambda toplam, x: toplam + x, sayilar, 0)


def toplam_baglanti_sum(galaksi: dict) -> int:
    #sum() kullanarak tüm bağlantıların toplam sayısını hesaplar.
    return sum(len(v) for v in galaksi["baglantilar"].values())


def yolculuk(gezegen: str, hiz: int = 1, yakit: int = 100) -> str:
    #Bir gezegende yolculuk bilgisi üretir.
    sure = yakit // hiz
    return f"{gezegen} hedefine hız={hiz} ile yola çıkıldı. Tahmini süre: {sure} birim."


# hizli_yolculuk: functools.partial ile hiz=3 sabit yeni fonksiyon
hizli_yolculuk = functools.partial(yolculuk, hiz=3)


if __name__ == "__main__":
    galaksi = _galaksiyi_yukle()

    # 1. Büyük harfli gezegenler (map ve liste üreteci):
    print("map ile:", buyuk_harfli_gezegenler_map(galaksi))
    print("liste üreteci ile:", buyuk_harfli_gezegenler_liste(galaksi))

    # 2. En az 2 bağlantılı gezegenler (filter ve liste üreteci):
    print("\nfilter ile:", iki_baglantili_filter(galaksi))
    print("liste üreteci ile:", iki_baglantili_liste(galaksi))

    # 3. Toplam bağlantı sayısı (reduce ve sum):
    print("\nreduce ile toplam:", toplam_baglanti_reduce(galaksi))
    print("sum ile toplam:", toplam_baglanti_sum(galaksi))

    # 4. partial – hizli_yolculuk:
    print("\nhizli_yolculuk:", hizli_yolculuk("sirius"))
    print("hizli_yolculuk:", hizli_yolculuk("centauri", yakit=50))
