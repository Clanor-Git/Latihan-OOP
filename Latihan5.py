from abc import ABC, abstractmethod

# Ini adalah KONTRAK. Semua turunan wajib punya method di bawah ini.
class GameUnit(ABC):
    @abstractmethod
    def serang(self, target):
        pass

    def info(self):
        pass

class Hero(GameUnit):
    def __init__(self, nama):
        self.nama = nama

    def serang(self, target):
        print(f"Hero {self.nama} menebas {target}!")
    def info(self):
        print(f"Saya adalah Hero: {self.nama}")
class Monster(GameUnit):

    def __init__(self, jenis):
        self.jenis = jenis
 
    def serang(self, target):
        print(f"Monster {self.jenis} menggigit {target}!")
    def info(self):
        print(f"Saya adalah Monster: {self.jenis}")
# -- Uji Coba --
# unit = GameUnit() # ERROR! Abstract class tidak bisa jadi objek.

h = Hero("Alucard")
m = Monster("Serigala")
h.info()
m.info()

#Pada class Hero, hapus (atau jadikan komentar #) seluruh
#blok method def serang(self, target):. Jalankan programnya.
#Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti
#pesan error Can't instantiate abstract class Hero with abstract method...?

#Arti Pesan Error: Python tidak bisa membuat objek dari class Hero karena class tersebut belum menyelesaikan/mengimplementasikan method abstrak serang() yang sudah diwajibkan oleh class induk .

#Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di Interface?

#Program tidak bisa dijalankan dan objek tidak akan pernah bisa dibuat sampai seluruh method abstrak yang diwajibkan oleh Interface/Abstract Class diimplementasikan.

#Coba aktifkan baris kode unit = GameUnit().
#Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
#Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?

#Class GameUnit adalah sebuah Abstract Class (kerangka/kontrak dasar) yang method-method di dalamnya (serang dan info) belum memiliki isi atau logika nyata.

#Berfungsi sebagai cetakan dasar (kontrak) untuk memastikan seluruh class turunan (seperti Hero dan Monster) memiliki standar method dan struktur yang sama.