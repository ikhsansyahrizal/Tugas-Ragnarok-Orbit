from abc import abstractmethod, ABC

merek = "Erigo"
ukuruan = "L"
warna = "Hitam"

def tagline():
    print("Erigo Local Pride")

def info(merek, ukuran, warna):
    print(f"Merek : {merek}, ukuran: {ukuran}, warna : {warna}")

info(merek, ukuruan, warna)
tagline()



#Abstraction
class Pakaian(ABC):
    def tagline(self, merek):
        print("Local Pride: ", merek)



#Encapsulation & Inheritance
class Baju(Pakaian):
    def __init__(self, imerek, iukuran, iwarna):
        self.imerek = imerek
        self.iukuran = iukuran
        self.iwarna = iwarna

    
    def info_pakaian(self):
        print("""
        Merek Pakaian : %s
        Ukuran Pakaian : %s
        Warna Pakaian : %s
        """ %(self.imerek, self.iukuran, self.iwarna))


baju_erigo1 = Baju("Erigos","L","Krem")
baju_erigo1.tagline("Erigo")
baju_erigo1.info_pakaian()



#Polymorphism
class Celana(Baju):
    def __init__(self, imerek, iukuran, iwarna, ijenis):
        super().__init__(imerek, iukuran, iwarna)
        self.ijenis = ijenis

    
    def review_celana(self):
        print("""
        Saya Andi dan celana merek %s ini sangat bagus,
        Ukuran yang saya pakai %s dengan warna %s
        Jenis celanaya %s.
        Overall Recommended sekali !!!
        """ %(self.imerek, self.iukuran, self.iwarna, self.ijenis))


celana_jeans1 = Celana("Jeans", "XL", "Hitam", "Pensil")
celana_jeans1.tagline("jeans")
celana_jeans1.info_pakaian()
celana_jeans1.review_celana()


