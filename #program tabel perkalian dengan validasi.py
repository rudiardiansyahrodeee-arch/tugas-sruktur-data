#program tabel perkalian dengan validasi nama

# input nama
nama_benar ="rudi"
nama = input("masukkan nama anda:") 
if nama == nama_benar:
    print("nama benar, lanju ke program...\n")
# input angka

angka = int(input("masukkan anngka:"))
     print("\n tabel perkalian:")
for in range(1,11):
    print(f"{angka}x {i} = {angka* i}")
else:
    print("silahkan coba lagi")