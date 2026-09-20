class Hero:
    def __init__(self, nama, hp_awal):

        self.__hp = hp_awal

    def get_hp(self):
        return self.__hp

    def set_hp(self, nilai_baru):
        if nilai_baru < 0:
            self.__hp = 0 
        elif nilai_baru > 1000:
            print("Cheat terdeteksi! HP dimaksimalkan ke 1000 saja.")
            self.__hp = 1000
        else:
            self.__hp = nilai_baru
    def diserang(self, damage):

        sisa_hp = self.get_hp() - damage
        self.set_hp(sisa_hp)
        print(f"{self.nama} terkena damage {damage}. Sisa HP:{self.get_hp()}")


hero1 = Hero("Layla", 100)
hero1.set_hp(-60)

print(hero1.get_hp()) 


print(f"Mencoba akses paksa: {hero1._Hero__hp}")

#Tugas analisis 4

#print(f"Mencoba akses paksa: {hero1._Hero__hp}")

#Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan
#teman mengapa Python masih mengizinkan akses ini (konsep Name Mangling)
#dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman
#yang baik.

#Hasil berhasil
#Mengapa Diizinkan : Python tidak mengunci variabel secara permanen, melainkan hanya mengubah nama __hp menjadi _Hero__hp secara otomatis di dalam sistem untuk mencegah bentrokan nama atribut saat pewarisan (inheritance
#Mengapa Tidak Boleh Dilakukan: Melanggar konsep Encapsulation, dapat merusak data karena memintas aturan validasi, dan menyalahi standar/etika pemrograman Python.

#Hasil Tanpa if/elif: Nilai HP Hero akan langsung menjadi -60
#Pentingnya Setter: Berfungsi sebagai filter/validasi untuk menjaga integritas data (Data Integrity), memastikan tidak ada data aneh/invalid (seperti HP minus atau cheat berlebihan) yang masuk ke dalam sistem game.