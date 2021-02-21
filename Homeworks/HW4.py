import random

class AdamAsmaca():
    def __init__(self):
        self.secilenKelime = ""
        self.tahmin = ""
        self.kelimeler = ["ananas", "portakal", "mandalina", "karpuz", "şeftali"]
        self.resim = ["""
                   +---+
                   |   |
                       |
                       |
                       |
                       |
                --------""","""
                   +---+
                   |   |
                   O   |
                       |
                       |
                       |
                --------""","""
                   +---+
                   |   |
                   O   |
                   |   |
                       |
                       |
                --------""","""
                   +---+
                   |   |
                   O   |
                  /|   |
                       |
                       |
                --------""","""
                   +---+
                   |   |
                   O   |
                  /|\  |
                       |
                       |
                --------""","""
                   +---+
                   |   |
                   O   |
                  /|\  |
                  /    |
                       |
                --------""","""
                   +---+
                   |   |
                   O   |
                  /|\  |
                  / \  |
                       |
                --------"""]
    def oyunaBasla(self, adim):
        print(self.resim[adim])
    
    def kelimeSec(self):
        self.secilenKelime = random.choice(self.kelimeler)
    
    def tahminOlustur(self):
        self.tahmin = "_" * len(self.secilenKelime)
    
    def adimIlerle(self, adim):
        print(self.resim[adim])
        
    def kelimeKontrol(self, kelime):
        if self.secilenKelime == kelime:
            return True
        else:
            return False
    
    def tahminYazdir(self):
        print(self.tahmin)
        
    def tahminDuzenle(self):
        index = random.randint(0,len(self.secilenKelime)-1)
        while True:
            if self.tahmin[index] == "_":
                self.tahmin = self.tahmin[:index] + self.secilenKelime[index] + self.tahmin[index + 1:]
                break;
            else:
                index = random.randint(0,len(self.secilenKelime)-1)
                
        
oyun = AdamAsmaca()
adim = 0
oyun.kelimeSec()
oyun.tahminOlustur()
oyun.oyunaBasla(adim)
oyun.tahminYazdir() 
adim += 1
while True:
    kullaniciKelime = input("Kelimeyi Tahmin Ediniz: ")
    if oyun.kelimeKontrol(kullaniciKelime):
        print("Tebrikler kazandınız.")
        break;
    if adim == 6:
        print("Kaybettiniz!!")
        break;
    oyun.adimIlerle(adim)
    oyun.tahminDuzenle()
    oyun.tahminYazdir()      
    adim += 1
    
print("Oynadığınız için teşekkürler.")
    
