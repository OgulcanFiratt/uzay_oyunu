def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    #Oyuncunun envanterindeki eşyaları metin olarak dönüştürür.
    esyalar = []
    
    if credits:
        esyalar.append("bol kredi")

    if engines:
        esyalar.append("hiperdrive")

    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""
    
    else:
        return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: list[str]) -> str:
    #Hedef menüsünü oluşturur.
    satirlar = ["Nereye gitmek istersin?"]
    
    for i, hedef in enumerate(hedefler, 1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)