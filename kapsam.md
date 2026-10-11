# Hafta 3 - Kapsam Notları

Oğulcan Fırat - 20253004003

## LEGB Sıralaması
Python bir değişkene bakarken sırayla şunlara bakar:
1. Local (fonksiyonun içi)
2. Enclosing (iç içe fonksiyon varsa dıştaki)
3. Global (dosyadaki ana değişkenler)
4. Built-in (Python'ın kendi fonksiyonları: print, len vb.)

---

## Dersteki 3 Örnek

### Örnek 1: Dışarıdaki değişkeni okuma
```python
x = 10

def yazdir():
    print("x:", x)

yazdir()
```
- **Tahminim:** 10 yazar.
- **Gerçek Sonuç:** `x: 10`
- **Nedeni:** Fonksiyonun içinde `x` diye bir şey tanımlamadığımız için gitti dışarıdaki (global) 10'u aldı.

---

### Örnek 2: Fonksiyon içinde aynı isimde değişken tanımlama
```python
x = 10

def degistir():
    x = 20
    print("İçerideki x:", x)

degistir()
print("Dışarıdaki x:", x)
```
- **Tahminim:** İçeride 20, dışarıda 10 yazar.
- **Gerçek Sonuç:** İçerideki x: 20, Dışarıdaki x: 10
- **Nedeni:** Fonksiyonun içindeki `x = 20` sadece o fonksiyonun içinde geçerli oldu (yerel kaldı). Dışarıdaki `x`'e dokunmadı.

---

### Örnek 3: UnboundLocalError Hatası
```python
x = 10

def hata():
    print("x:", x)
    x = 20

hata()
```
- **Tahminim:** Hata verir ya da 10 yazar.
- **Gerçek Sonuç:** `UnboundLocalError: cannot access local variable 'x' where it is not associated with a value`
- **Nedeni:** Fonksiyonun altında `x = 20` yazdığımız için Python bu fonksiyon içindeki `x`'i yerel değişken sanıyor. Ama biz daha değer atamadan önce üst satırda `print(x)` yazdırdığımız için Python "henüz değeri atanmamış değişkeni okumaya çalışıyorsun" diyerek hata veriyor.

---

## `depo=[]` Hatası
```python
def yakit_ekle(miktar, depo=[]):
    depo.append(miktar)
    return depo
```
- **Neden hatalı?** Python'da varsayılan liste (`depo=[]`) sadece bir kere oluşturuluyor. Fonksiyonu her çağırdığımızda sıfırlanmıyor, eski çağrıdaki sayılar listenin içine eklenmeye devam ediyor.
- **Çözüm:** `depo=None` yapıp fonksiyonun içinde `if depo is None: depo = []` yazınca her seferinde yeni liste açılıyor.
