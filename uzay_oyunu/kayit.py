def  gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler) -> str:
    #Görev kaydını oluşturur. * ve ** parametrelerini kullanır.
    satirlar = [f"[{oncelik}] {baslik}"]
    
    #Adımları yine enumerate ile numaralandırır:
    for i, adim in enumerate(adimlar,1):
        satirlar.append(f" {i}. {adim}")
    
    #Adımlardan sonraki sözlük verilerini ekler:
    for anahtar, deger in ekler.items():
        satirlar.append(f" {anahtar}: {deger}")

    return "\n".join(satirlar)

    
if __name__ == "__main__":
    # 1. Doğrudan parametre vererek çağırma:
    print(gorev_kaydi("Kara deliğe atla", "Kredi kazan", "Pilot bul", "Hiperdrive al", oncelik="YÜKSEK", sorumlu="Ayşe"))

    # 2. Listeyi (*) ve Sözlüğü (**) açarak (unpacking) çağırma:
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekstra = {"sorumlu": "Ayşe"}
    print(gorev_kaydi("Kara deliğe atla", *adimlar_listesi, oncelik="YÜKSEK", **ekstra))
