# Parent Class
class Hero:
    def __init__(self, nama):
        self.nama = nama
    def serang(self):
        print("Hero menyerang dengan tangan kosong.")
 
class Mage(Hero):
    def serang(self):
        print(f"{self.nama} (Mage) menembakkan Bola Api! Boom!")
 
class Archer(Hero):

    def serang(self):
        print(f"{self.nama} (Archer) memanah dari jauh! Jleb!")
 
class Fighter(Hero):
    def serang(self):
        print(f"{self.nama} (Fighter) memukul dengan pedang! Slash!")
 
pasukan = [
Mage("Eudora"),
Archer("Miya"),
Fighter("Zilong"),
Mage("Gord")
]
print("--- PERANG DIMULAI ---")
 
for i in pasukan:i.serang()

#Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf
#pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class
#baru bernama Healer(Hero).
#Isi method serang milik Healer dengan: print(f"{self.name} tidak
#menyerang, tapi menyembuhkan teman!").
#Masukkan objek Healer ke dalam list pasukan.
#Pertanyaan: Apakah program berjalan lancar?
#Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer
#ketika harus mengupdate game dengan karakter baru di masa depan?

#Apakah Program Berjalan Lancar: Ya, program berjalan lancar tanpa error. Objek Healer akan diproses secara otomatis oleh perulangan for dan mencetak teks penyembuhan yang dibuat.
#Keuntungan Polimorfisme: Membuat kode sangat skalabel dan fleksibel. Programmer bisa menambah puluhan jenis karakter baru di masa depan tanpa perlu mengubah logika perulangan atau struktur program yang sudah ada

#Konsistensi Penamaan: Ubah nama method serang pada class Archer
#menjadi tembak_panah. Jalankan program.
#Pertanyaan: Apa yang terjadi?
#Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan
#berbagai Child Class harus persis sama?

#Output yang keluar adalah "Hero menyerang dengan tangan kosong." dan method tembak_panah() tidak akan pernah terpanggil secara otomatis oleh looping.
#Polimorfisme bergantung pada nama method yang identik antara parent dan child class agar satu perintah pemanggilan (seperti pahlawan.serang()) dapat mengeksekusi perilaku yang tepat sesuai jenis objeknya