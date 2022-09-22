#tugas 1 algo
#alfarizqi wira anadyar
#21/9/2022

#pembukaan
print('Program ini akan menghitung luas dan keliling bangun datar tersebut: ')
nama =input('Tuliskan nama: ')
NIM =input('NIM: ')
prodi = input ('Program studi: ')
sklh = input('Nama sekolah/kampus asal: ')

#pemilihan
print()
print('Pilihan bangun datar: ')
print('[P]-Persegi empat')
print('[T]-Trapesium')
print('[J]-Jajar genjang ')
print('[L]-Lingkaran ')
print('[S]-Segitiga sama sisi ')
bangun = input('Bangun Ruang [P/T/J/L/S]: ')
satuan = input('Satuan yang di gunakan(meter/inchi/...): ')



#prosesing
print()
if bangun == 'P':
    tinggi = int(input('Tinggi: '))
    lebar = int(input('Lebar: '))
    luas = tinggi*lebar
    keliling = (tinggi+lebar)*2
    print('Luas persegi empat: ',luas, satuan)
    print('keliling persegi: ',keliling, satuan)
elif bangun == 'T':
    atas = int(input('Sisi atas: '))
    bawah = int(input('Sisi bawah: '))
    samping = int(input('Sisi samping: '))
    tinggi = int(input('Tinggi: '))
    luas = ((atas+bawah)/2)*tinggi
    keliling = (samping*2)+atas+bawah
    print('Luas trapesium: ',luas, satuan)
    print('keliling trapesium: ',keliling, satuan)
elif bangun == 'J':
    lebar = int(input('Lebar: '))
    samping = int(input('Sisi samping: '))
    tinggi = int(input('Tinggi: '))
    luas = lebar*tinggi
    keliling = (lebar+samping)*2
    print('Luas jajar genjang: ',luas, satuan)
    print('keliling jajar genjang: ',keliling, satuan)
elif bangun == 'L':
    jari = float(input('Jari-jari: '))
    luas = jari*jari*3.14
    keliling = 2*jari*3.14
    print('Luas lingkaran: ',luas, satuan)
    print('keliling lingkaran: ',keliling, satuan)
elif bangun == 'S':
    sisi = int(input('Sisi: '))
    tinggi = int(input('Tinggi: '))
    luas = (1/2)*sisi*tinggi
    keliling = sisi*3
    print('Luas segitiga: ',luas, satuan)
    print('keliling segitiga: ',keliling, satuan)
else: 
    print('Maaf kami tidak mengerti apa yang anda maksud.')
    print('Harap memasukan input di "Bangun Ruang [P/T/J/L/S]: " sesuai opsi dan menggunakan huruf kapital.')

#penutup
print('Terima kasih', nama,',',NIM, 'dari', sklh, 'dengan program studi', prodi)
print('telah menggunakan program saya')
print()
print('Programmer: ')
print('Nama:Alfarizqi Wira Anadyar')
print('NIM:065002200034')
print('Program Studi: Sistem Informasi')
print('Jangan lupa follow @alfarizqiwira')