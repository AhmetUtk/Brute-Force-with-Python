import itertools

def brutForce(len, karakter, cikti="yazi.txt"):
    try:
        with open(cikti, "w") as file:
            for combination in itertools.product(karakter, repeat=uzunluk):
                password = ''.join(combination)
                file.write(password + "\n")
        print(f"{len}-uzunluğundaki şifre kombinasyonları {cikti} dosyasına kaydedildi.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Kullanıcıdan şifre uzunluğunu ve karakterler listesini alın
uzunluk = int(input("Şifre uzunluğunu girin: "))
karakter = input("Karakterleri girin: ")


# Karakterlerin bir liste olarak saklanması
karakterListe = list(karakter)

# Fonksiyonu çağırarak kombinasyonları oluştur ve dosyaya kaydet
brutForce(uzunluk, karakterListe)