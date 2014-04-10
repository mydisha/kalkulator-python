import sys
import os

def pindah(lokasi):
	global nomor
	nomor = lokasi

def clear():
	os.system('cls')

def keluar():
	sys.exit()

def ulang():
	tanya = raw_input("Apakah anda ingin mengulang [y/n] ? ")
	if tanya == "y" or "Y":
		pindah(0)
	elif tanya == "n" or "N":
		keluar()
	else:
		ulang()

def buatgaris():
 	print "-------------------"

nomor = 0

while True :
 if nomor == 0 :
	clear()
	buatgaris()
	print "  Aplikasi Kalkulator"
	buatgaris()
	print "1. Menghitung Segitiga"
	print "2. Menghitung Lingkaran"
	print "3. Menghitung Balok"
	print "4. Keluar Program"
	print "\n"

	pilih = int(raw_input("Masukkan pilihan Anda [1-4] : "))

	if pilih ==  1 :
		pindah(1)
	elif pilih == 2 :
		pindah(2)
	elif pilih == 3 :
		pindah(3)
	elif pilih == 4 :
		pindah(4)
	else :
		pindah(0)

 elif nomor == 1:
 	clear()
 	buatgaris()
	print "Menghitung Segitiga"
	buatgaris()
	alas = int(raw_input("Masukkan Alas : "))
	tinggi = int(raw_input("Masukkan Tinggi : "))
	hitung = (float(alas) * float(tinggi)) / 2
	print "Hasilnya adalah : ", hitung
	ulang()

 elif nomor == 2:
 	clear()
 	buatgaris()
 	print "Menghitung Lingkaran"
 	buatgaris()
 	phi = 3.14
 	jari2 = int(raw_input("Masukkan Jari-Jari : "))
 	hitung = float(phi * float((jari2**2)))
 	print "Hasilnya adalah : ", hitung
 	ulang()

 elif nomor == 3 :
 	clear()
 	buatgaris()
 	print "Menghitung Balok"
 	buatgaris()
 	panjang = int(raw_input("Masukkan Panjang : "))
 	lebar = int(raw_input("Masukkan Lebar : "))
 	tinggi = int(raw_input("Masukkan Tinggi : "))
 	hitung  = float(panjang * lebar * tinggi)
 	print "Hasilnya adalah : ", hitung
 	ulang()
 elif nomor == 4 :
 	clear()
 	keluar()
 else :
 	keluar()
