









import sys
import os

import datetime

lama_hari=0


#selamat datang
def print_menu():
    print(1* "-")
    print()
    print('\t','     HOTEL MELATI SOLO BARU ')
    print()
    print('\t','---------Selamat Datang----------')
    print()
    print('Jl.Solo baru No.900, kode pos 29112 No HP. 0001122')
    print('\t','      Solo baru Surakarta')
    print()
    print('\t',' Hotel bintang 3 dengan keunggulan: ')
    print('\t','           Nyaman')
    print('\t','            Aman')
    print('\t','           Bersih')
    print('\t','            Asri')
    print()
    print(50* "-")
    print()
    
print_menu()


  
print()  
 
#masuk sistem
def sistem():
    print('Pilih yang anda inginkan ?')
    print()
    print('1. CHECK IN')
    print('2. keluar program') 
    pilihan = input("Pilih yang anda inginkan (1/2):  ")
    if pilihan == "1":
        print("Dimohon mengisi tanggal")
    else :
        sys.exit()
        
sistem()
    

print("--------------------")  
print()  

#waktu inap
def waktuinap(): 
    print('\t','Masukkan tanggal CHECK-IN')
    tanggalmasuk = int(input("Masukkan TANGGAL (1-31):"))
    bulanmasuk = int(input("Masukkan BULAN (1-12):"))
    tahunmasuk = int(input("Masukkan TAHUN (2020-2050):"))
    
    print('\t','Masukkan tanggal CHECK-OUT')
    tanggalkeluar = int(input("Masukkan TANGGAL (1-31):"))
    bulankeluar = int(input("Masukkan BULAN (1-12):"))
    tahunkeluar = int(input("Masukkan TAHUN (2020-2050):"))
    
    keluar = datetime.datetime(tahunkeluar, bulankeluar, tanggalkeluar)
    masuk = datetime.datetime(tahunmasuk, bulanmasuk, tanggalmasuk)
    lama = keluar - masuk
    print("Anda menginap selama", lama)
    
waktuinap()


print("--------------------")  
print()  

#jumlah orang
def jumlahorang():
    print('\t',"Masukkan jumlah penghuni kamar")
    Dewasa = input("Jumlah dewasa(0-5): ")
    Anak = input("Jumlah anak(0-5): ")
    Bayi = input("Jumlah bayi(0-5): ")
    print("Jumlah penghuni kamar sebanyak", Dewasa, "dewasa, ", Anak, "anak, dan ", Bayi, "bayi")
    
jumlahorang()
    

print("--------------------")  
print()  
    
#tipe kamar hotel
def jenis():   
    print('\t',"Pilih jenis hotel yang anda inginkan")
    print()
    print('Jenis kamar hotel (1-3)?')
    print()
    from random import randint
    for _ in range(1):
        jumlahk = randint(0, 20)
        print('1. Reguler -', jumlahk,"Available")
    from random import randint
    for _ in range(1):
        jumlahk = randint(0, 15)
        print('2. Deluxe -', jumlahk,"Available")
    from random import randint
    for _ in range(1):
        jumlahk = randint(0, 10)
        print('3. Suite -', jumlahk,"Available")
    print()
        
    jenis = input("Jenis kamar hotel? ")
    if jenis == "1":
        bed = input("1.Queen atau 2.Twin (1/2)? ")
        if bed == "1":
            from random import randint
            for _ in range(1):
                harga = randint(400, 450)
                print("Tarif",harga,".000 rupiah")
        elif bed == "2":
            from random import randint
            for _ in range(1):
                harga = randint(420, 460)
                print("Tarif",harga,".000 rupiah")
        
    elif jenis == "2":
        bed = input("1.Queen atau 2.Twin (1/2)? ")
        if bed == "1":
             from random import randint
             for _ in range(1):
                harga = randint(650, 700)
                print("Tarif",harga,".000 rupiah")
        elif bed == "2":
            from random import randint
            for _ in range(1):
                harga = randint(680, 720)
                print("Tarif",harga,".000 rupiah")
        
    elif jenis == "3":
        bed = input("1.Queen atau 2.Twin (1/2)? ")
        if bed == "1":
            from random import randint
            for _ in range(1):
                harga = randint(900, 960)
                print("Tarif",harga,".000 rupiah")
        elif bed == "2":
            from random import randint
            for _ in range(1):
                harga = randint(920, 980)
                print("Tarif",harga,".000 rupiah")
                
jenis()


print("--------------------")  
print()  

#identitas diri
iterasi = True
print('\t',"WAJIB MEMPUNYAI IDENTITAS JIKA AKAN MELAKUKAN PEMBAYARAN!")

while iterasi == True:
    identitas = input("Apakah anda mempunyai identitas(KTP/Paspor/SIM)? (y/n)")
    if identitas =="y":
        iterasi = False
    else :
        iterasi = True 
        
        
print("--------------------")  
print()   
  
#list identitas diri 
print('\t',"Mohon untuk mengisi identitas dengan benar")
nama = input("Nama : ")
nomor_id = input("Nomor ID : ")
no_telp = input("No Telp : ")
alamat = input("Alamat : ")
identitas = ['Nama:', nama,
             'Nomor ID:', nomor_id ,
             'No Telp:', no_telp,
             'Alamat: ', alamat]
print(identitas)
print("Kebenaran isi identitas ini akan menjadi jaminan")


print("--------------------")  
print()  

#jenis pembayaran
def pembayaran():
    print('\t',"SILAKAN MELAKUKAN PEMBAYARAN")
    print()
    print("Pilih metode pembayaran yang akan Anda lakukan:")
    print('1. Cash')
    print('2. Debit Card')
    
    #pembayaran dengan Cash
    pilih = input("Pilih yang anda inginkan (1/2):  ")
    if pilih == "1":
        print("""
        Terima kasih telah melakukan reservasi di hotel kami
        Selamat menikmati penginapan yang nyaman
        Semoga hari Anda menyenangkan:)
        """)

    #pembayaran dengan Debit Card
    else:
        iterasi = True
        while iterasi == True:
            saldo = input('Apakah saldo mencukupi? (y/n)')
            if saldo == 'y':
                print("""
                Terima kasih telah melakukan reservasi di hotel kami
                Selamat menikmati penginapan yang nyaman
                Semoga hari Anda menyenangkan:)
                """)
                iterasi = False
 
            #saldo tidak mencukupi
            else :
                print ("""
                Mohon maaf sisa saldo Anda tidak mencukupi untuk melakukan reservasi ini.
                Silahkan gunakan debit card lain atau menggunakan metode pembayaran lain
                """)
                ubah = input ('Ingin mengubah metode pembayaran atau mengganti debit card?')
                if ubah == 'y':
                    change = input('Ubah metode pembayaran menjadi cash?')
                    if change == 'y':
                        print("""
                        Terima kasih telah melakukan reservasi di hotel kami
                        Selamat menikmati penginapan yang nyaman
                        Semoga hari Anda menyenangkan:)
                        """)
                    else :
                        ganti = input ('Ingin mengganti debit card?')
                        if ganti == 'y':
                            iterasi = True
                        else :
                            sys.exit()
                else :
                    sys.exit()

pembayaran() 
