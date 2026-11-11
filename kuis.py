
# Program Kelulusan Ujian Matematika

# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Menentukan target nilai berdasarkan nama
if nama.lower() == "andi":
    target = 70
elif nama.lower() == "budi":
    target = 75
elif nama.lower() == "citra":
    target = 80
else:
    print("Nama mahasiswa tidak terdaftar!")
    exit()

print("\nNama Mahasiswa :", nama)
print("Target Nilai   :", target)

# Inisialisasi variabel
percobaan = 1
lulus = False

# Perulangan maksimal 3 kali
while percobaan <= 3:
    nilai = int(input(f"Masukkan nilai ujian ke-{percobaan}: "))

    # Pengecekan nilai
    if nilai >= target:
        lulus = True
        break
    else:
        print("Nilai belum mencapai target.")
        if percobaan < 3:
            print("Silakan mengikuti remedial!\n")

    percobaan += 1

# Menampilkan hasil akhir
print("\n===== HASIL UJIAN =====")
print("Nama Mahasiswa :", nama)
print("Target Nilai   :", target)
print("Jumlah Percobaan:", percobaan)

if lulus:
    print(f"{nama} berhasil lulus!")
else:
    print(f"{nama} tidak lulus setelah 3 kali percobaan.")
