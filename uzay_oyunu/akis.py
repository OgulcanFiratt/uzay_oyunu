import itertools
import functools
from pathlib import Path


def fibonacci():
    #Sonsuz Fibonacci sayıları üreten üreç.
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int):
    #Her next() çağrısında yakıtı tuketim kadar azaltıp kalan yakıtı üretir; 0'a inince durur.
    while yakit > 0:
        yakit = max(0, yakit - tuketim)
        yield yakit


def satirlari_oku(yol: str):
    #Dosyayı satır satır okur; boş ve # ile başlayan satırları atlar.
    with open(yol, encoding="utf-8") as dosya:
        for satir in dosya:
            satir = satir.strip()
            if satir and not satir.startswith("#"):
                yield satir


def ayristir(satirlar):
    #Her satırdan (kaynak, hedef, yakit) demeti üretir.
    for satir in satirlar:
        yon, yakit_str = satir.rsplit(" ", 1)
        kaynak, hedef = yon.split(" -> ")
        yield kaynak.strip(), hedef.strip(), int(yakit_str.strip())


def uzun_yolculuklar(kayitlar, esik: int):
    #Yakıt değeri eşikten büyük olan kayıtları filtreler.
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit


def rota_sayaci(baglantilar: dict[str, list[str]]):
    #Verilen bağlantı haritası için önbellekli rota sayma fonksiyonu döner.
    @functools.lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        #Gezegenden başlayıp tam adim yolculuk yapan farklı rotaların sayısını hesaplar.
        if adim == 0:
            return 1
        komsular = baglantilar.get(gezegen, [])
        return sum(rota_sayisi(k, adim - 1) for k in komsular)

    return rota_sayisi


if __name__ == "__main__":
    import json

    # 1. Fibonacci denemesi:
    g = fibonacci()
    print("İlk 3 değer (next ile):", next(g), next(g), next(g))
    print("İlk 12 değer (islice):", list(itertools.islice(fibonacci(), 12)))
    print("100'den küçük değerler:", list(itertools.takewhile(lambda x: x < 100, fibonacci())))

    # 2. Yakıt göstergesi denemesi:
    print("\nYakıt göstergesi (100, 30):", list(yakit_gostergesi(100, 30)))

    # 3. Boru hattı denemesi:
    seyir_yolu = Path(__file__).parent.parent / "veri" / "seyir.txt"
    toplam = sum(y for _, _, y in ayristir(satirlari_oku(str(seyir_yolu))))
    print(f"\nToplam yakıt maliyeti: {toplam}")
    kayitlar = ayristir(satirlari_oku(str(seyir_yolu)))
    print("Uzun yolculuk hedefleri (>10):", [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)])

    # 4. Önbellekli rota sayacı denemesi:
    galaksi_yolu = Path(__file__).parent / "galaksi.json"
    with open(galaksi_yolu, encoding="utf-8") as f:
        galaksi = json.load(f)
    say = rota_sayaci(galaksi["baglantilar"])
    print(f'\nRota sayıları: {say("dünya", 3)}, {say("dünya", 10)}, {say("dünya", 40)}')
    print("Önbellek bilgisi:", say.cache_info())
