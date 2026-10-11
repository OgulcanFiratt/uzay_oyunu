def hamle_sayaci():
    #Her çağrıldığında 1 artan sayaç fonksiyonu döner.
    hamle = 0

    def sayac() -> int:
        nonlocal hamle
        hamle += 1
        return hamle

    return sayac


def en_bagli_gezegenler(galaksi: dict) -> list[str]:
    #Gezegenleri bağlantı sayısına göre çoktan aza, eşitlikte alfabetik sıralar.
    gezegenler = galaksi.get("gezegenler", [])
    baglantilar = galaksi.get("baglantilar", {})

    return sorted(
        gezegenler,
        key=lambda g: (-len(baglantilar.get(g, [])), g)
    )


if __name__ == "__main__":
    # 1. Hamle sayacı denemesi:
    sayac = hamle_sayaci()
    for _ in range(13):
        toplam = sayac()
    print(f"Oyunu {toplam} hamlede bitirdin!")

    # 2. En bağlı gezegenler denemesi:
    ornek_galaksi = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius", "orion"],
            "centauri": ["dünya", "sirius", "orion"],
            "sirius": ["dünya", "centauri", "orion", "kara_delik"],
            "orion": ["centauri", "sirius"],
            "kara_delik": ["sirius"],
        },
    }
    print("En bağlı gezegenler:", en_bagli_gezegenler(ornek_galaksi))
