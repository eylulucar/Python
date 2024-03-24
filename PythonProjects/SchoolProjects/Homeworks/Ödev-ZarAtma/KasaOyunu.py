

#KasaOyunu-While_DöngülüVersiyon-Eylul.py

#  Kasa Oyunu
#  Yönergede Kasa Oyunu'nu While döngüsü kullanarak yapmam isteniyor.

# Yönergede ilk işlem 1, son işlem 57 olarak verilmiş. Ondan Atılan Zar sayısı maksimum 6 diye ayarlamadım.
# Yönergede Kasanın 2 atması halinde Yapılması Gerekenleri koda dökün deniyor.
# AMAÇ kasanın sonuçta 2 vermesi.
# Zarlar hileli:), hep Batu kazanır ve Ali, Can hep kaybeder:)

from time import sleep # Bu modülü kullanarak, programın belirli bir süre durmasını sağlayabiliriz.


print("\n\tKasa Oyununa Hoş geldiniz")
sleep(1)
print("\n\tWelcome to the Card Game")
sleep(1)
print("\n\tCe jeu est le jeu de la caisse.")
sleep(1)
print("\nBu Oyun, Kasa Oyunu'dur. Ve eğer Kasa 2 atarsa, ne olacağını simüle eder.")
sleep(1)
print("\nThis game simulates what happens if the bank throws 2.")
sleep(1)
print("\nCe jeu simule ce qui se passe si la banque jette 2.")
sleep(1)

print("\nOyun başlıyor...")
sleep(1)
print("Hayali oyuncularımız Ali, Batu ve Can'a başlangıçta 0 TL verilmiştir.")
sleep(1)

# Başlangıç durumu
GelenZar = 2 # Yönergede Kasanın zar olarak 2 atması isteniyor.
oyuncular = {'Ali': 0, 'Batu': 0, 'Can': 0}

# While döngüsü
while True:
    # DUR komutunu kontrol et
    print("Kasa Oyunu- Zar Atma\n")
    print("\tZar atılıyor...")
    sleep (1)
    print("\nZar atıldı. Ve Yönerge gereği Kasa zar olarak 2 atacak hep:)")
    print("Zarlar hileli:)") # Zarlar hileli:), hep Batu kazanır ve Ali, Can hep kaybeder:)
    sleep (1)
    kasa_toplam_para = 0  # Kasa toplam para miktarını tutar
    print("Kasa pozisyonu:", kasa_toplam_para)
    dur_komutu = input("ZAR Atmaya DEVAM mı? Çıkmak isterseniz tercihte bulunun? (E/H): ")
    if dur_komutu.upper() == 'E':
        break  # DUR komutu geldiyse döngüden çık
    # Kasa zar atar, 2 gelmediği sürece döngü devam eder.
    zar_sonucu = 2 # Yönergede KAsanın 2 atması halinde Yapılması Gerekenleri koda dökün deniyor.
    sayac = 1  # Kaçıncı zar atışı olduğunu sayar
    
    kasa_toplam_para += sayac
    
    # Kasa zar sonucunu kontrol eder
    
    if zar_sonucu == 2:
        # DUR komutunu görmediği sürece devam eder
        print("Kasa 2 attı. Yapılacak adımlar:")
        sleep (1)
        print("- Yönergedeki Adımları takip et: ")
        sleep (1)
        print("- 16'ya Git")
        sleep (1)
        print("Batu'ya 90 TL ver.")
        sleep (1)
        oyuncular["Batu"] += 90
        print("Batu'ya 90 TL verildi.")
        sleep (0.5)

# Oyunun son durumu
print("Oyun bitti. Kasa son pozisyon:", kasa_toplam_para)
sleep (1)
print("Oyuncu durumları:", oyuncular)
sleep (0.5)
print("Oyun sona erdi.")

