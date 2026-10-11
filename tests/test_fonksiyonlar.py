from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_metni():
    #Envanter metni dolu olduğunda dönecek metin. 
    sonuc = envanter_metni(True, False, True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_bos():
    #Envanter metni boş olduğunda dönecek metin.
    sonuc = envanter_metni(False, False, False)
    assert sonuc == ""


def test_hedef_menu():
    hedefler = ["centauri", "sirius"]
    beklenen_metin = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen_metin
