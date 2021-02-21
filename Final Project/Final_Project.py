class Tarifler():
    def __init__(self):
        self.tuz = 0
        self.yag = 0
        self.hazir = False
        self.yemekAdi = ""

    def Pisirme(self):
        print(self.yemekAdi + " yemeğiniz pişiriliyor.") 
        self.hazir = True
        print(self.yemekAdi + " yemeğiniz hazır.\n")
        
    def TuzEkle(self):
        self.tuz += 1
        print(self.yemekAdi + " yemeğinize tuz ekleniyor.")
        
    def YemegiKaristir(self):
        print(self.yemekAdi + " yemeğiniz karıştırılıyor.")
    
    def YagEkle(self):
        self.yag += 1
        print(self.yemekAdi + " yemeğinize yağ ekleniyor.")

    def Miktar(self):
        if(self.yemekAdi == "Pilav"):
            print("Pilav'a 2 bardak pirinç, bir yemek kaşığı yağ, bir çay kaşığı tuz, 3 su bardağı su eklemelisiniz.")
        if(self.yemekAdi == "Mantar Çorbası"):
            print("Mantar çorbasına 1 yemek kaşığı yağ, 500gr mantar, 1 çay bardağı süt, yarım çay bardağı un, 1 çay kaşığı tuz eklemelisiniz.")
        if(self.yemekAdi == "Tavuk"):
            print("500gr tavukları doğrayın 1 yemek kaşığı yağ, 1 çay kaşığı tuz, isteğinize göre baharat eklemelisiniz.")


class Pilav(Tarifler):
    def __init__(self):
        super().__init__()
        self.su = 0
        self.yemekAdi = "Pilav"

    def PirincEkle(self):
        print(self.yemekAdi + "'a pirinç ekleniyor.")
    
    def SuEkle(self):
        self.su += 1
        print(self.yemekAdi + "'a su ekleniyor.")
              
        
        
        
class MantarCorbasi(Tarifler):
    def __init__(self):
        super().__init__()
        self.sut = 0
        self.mantar = 0
        self.un = 0
        self.yemekAdi = "Mantar Çorbası"
        
    def SutEkle(self):
        self.sut += 1
        print(self.yemekAdi + "'na süt ekleniyor.")
    
    def MantarEkle(self):
        self.mantar += 1
        print(self.yemekAdi + "'na mantar ekleniyor.")

    def UnEkle(self):
        self.un += 1
        print(self.yemekAdi + "'na un ekleniyor.")

class Tavuk(Tarifler):
    def __init__(self):
        super().__init__()
        self.baharat = 0
        self.yemekAdi = "Tavuk"
    
    def BaharatEkle(self):
        self.baharat += 1
        print(self.yemekAdi + "'a baharat ekleniyor.")
        
    def TavuklariDogra(self):
        print(self.yemekAdi + "'lar doğranıyor.")
        
pilav = Pilav()
corba = MantarCorbasi()
tavuk = Tavuk()

pilav.Miktar()

pilav.PirincEkle()
pilav.YagEkle()
pilav.TuzEkle()
pilav.SuEkle()
pilav.YemegiKaristir()
pilav.Pisirme()

corba.Miktar()

corba.YagEkle()
corba.MantarEkle()
corba.SutEkle()
corba.UnEkle()
corba.TuzEkle()
corba.YemegiKaristir()
corba.Pisirme()

tavuk.Miktar()

tavuk.TavuklariDogra()
tavuk.YagEkle()
tavuk.TuzEkle()
tavuk.BaharatEkle()
tavuk.YemegiKaristir()
tavuk.Pisirme()
        
        