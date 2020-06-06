#
#
#
#
#
#




from datetime import datetime, date
from random import randint
import os
import sys
checkin, checkout = None, None
loop = True

def print_menu(): # tampilan menu awal
    print()
    print('\t','      HOTEL MELATI SOLO BARU ')
    print()
    print('\t','---------Selamat Datang----------')
    print()
    print('Jl.Solo baru No.900, kode pos 29112 No HP. 08232111')
    print('\t','      Solo Baru Surakarta')
    print()
    print('\t',' Hotel bintang 3 dengan keunggulan: ')
    print('\t','           Nyaman')
    print('\t','            Aman')
    print('\t','           Bersih')
    print('\t','            Asri')
    print()
    print('======================================================')
    print('Pilih yang Anda inginkan :')
    print()
    print('1. CHECK IN')
    print('2. Keluar program')
    print()
    
#program dimulai

while loop:
    print_menu() #memanggil def menu diatas
    pilihan = int(input('Masukkan pilihan [1/2]: '))
    print() 
    os.system('cls') #membersihkan layar dalam shell
    if (pilihan == 1):  #ketika memilih 'checkIn'
        print()
        print('\t','[ ISI BIODATA PENGINAP ]')
        print('------------------------------------')
        print()
        nama = input('Masukkan nama lengkap penginap : ').upper()
        nohp = input('Masukkan No HP penginap : +62 ')
        if len(nohp) != 11 and len (nohp) != 13: 
            # ketika no hp tidak sama dengan 11/13 digit, program akan menolak.
            os.system('cls')
            print('No Hp Anda tidak terdaftar')
            continue
        ktp = input ('Apakah Anda memiliki kartu identitas KTP/SIM (y/n) : ')
        if ktp == 'n':
            sys.exit('\nError : Anda harus memiliki kartu identitas untuk menginap')      
             # penginap/tamu harus memiliki kartu identitas untuk menginap, jika tidak punya, TIDAK boleh menginap.
        elif ktp == 'y':
            kk = input('Masukkan No identitas kartu : ')
            tl = input("Masukkan Tempat lahir Anda : ").upper()
            tt = input ('Masukkan tanggal lahir Anda (dd-mm-yyyy) : ')
            print()
            os.system('cls')
        else:
            os.system('cls')
            input('\nError : Anda harus memilih antara (y/n)')
            continue
    elif (pilihan == 2):
        sys.exit('\nInformasi : Anda telah keluar program')
    else:
        print('Pilihan yang Anda masukkan salah, silahkan coba lagi')
        continue
    #mengisi tipe kamar sesuai keinginan penginap/tamu
    print()
    print('\t','ISI TIPE KAMAR SESUAI DENGAN PILIHAN PENGINAP')
    print('======================================================')
    print()
    print('1. Regular')
    print('2. Deluxe')
    print('3. Suite')
    print('4. President suite')

    jenis = ['Regular','Deluxe ','Suite','President Suite']
    #jenis kamar berbentuk list akan dipanggil sesuai pilihan pengunjung
    jenisPerMalam = [150000, 200000, 250000, 300000]
    #tarif permalam untuk setiap jenis kamar dalam bentuk list akan dipanggil untuk menentukan tarif akhir...
    
    tipe = int(input('Masukkan tipe kamar yang Anda pilih : '))
    os.system('cls')
    if (tipe == 1):
        kamar = jenis[0]
      
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn :  ")
     
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
                #format tanggal
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
                #ketika format tanggal yang dimasukkan tidak sesuai, akan memunculkan pesan tersebut.

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut :  ")

            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        #untuk menghitung rentang hari tamu menginap.
        waktu =(waktuMenginap.days)
        global tarif
        tarif = (jenisPerMalam[0] * waktu)

    elif (tipe == 2):
        kamar = jenis[1]

        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn :  ")
 
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut : ")

            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        tarif = (jenisPerMalam[1] * waktu)

    elif (tipe == 3):
        kamar = jenis[2]

        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn : ")
       
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
                
        while checkout is None: 
            tanggal = input("Masukkan tanggal CheckOut : ")
                
            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        tarif =(jenisPerMalam[2] * waktu)


    elif (tipe == 4):
        kamar = jenis[3]
     
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn : ")
            
            try:
                checkin = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut : ")

            try:
                checkout = datetime.strptime(tanggal, "%d %m %Y")
            except ValueError:
                print("Harus berformat \"<hari> <bulan> <tahun>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        tarif = (jenisPerMalam[3] * waktu)

        
        
    #masuk kebagian kwitansi pembayaran
    print()
    print()
    print('\t','KWITANSI PEMBAYARAN RESERVASI HOTEL')
    print('---------------------------------------------')
    print()
    print('\t','Nama : '+ str(nama))
    print()
    print('\t','No HP : (+62)'+ str(nohp))
    print()
    print('\t','No Identitas : '+ str(kk))
    print()
    print('\t','TTL : '+ str(tl) + ','+ str(tt))
    print()
    print('\t','Tipe kamar : '+ str(kamar))
    print()
    for _ in range(1):
        kamar = randint(1, 20)
        print('\t','Kunci kamar nomor :',kamar)
    print()
    print('\t','Waktu : '+ str(waktu)+ ' Malam')
    print()
    print('\t','Biaya : '+ 'Rp.' + str(tarif)+',00-')
    print()
    print('\t','Bayar dengan uang pas')
    print()
    print()
    print('Terima kasih atas kepercayaan yang Anda berikan kepada kami, semoga Anda senang')
    print()

    print('=======================================================')

    def pengecekanUlang():
    #berfungsi agar memastikan data yang diinputkan oleh resepsionis benar
        print('Silahkan cek data diatas terlebih dahulu')
        pilih = input("Apakah data tersebut sudah sesuai? [y/n]: ")
        if pilih == 'y':
            print()
        else:
            os.system('cls')
            print('Silahkan ulang dari awal, pastikan data yang Anda isi BENAR')
            sys.exit()
            #ketika terjadi kesalahan dalam pengisian data, program akan mengulan dari awal

    pengecekanUlang()

    #masuk ke bagian pembayaran
    #resepsionis akan menawarkan 2 opsi pembayaran
    while loop: 
        print("[SILAHKAN MELAKUKAN PEMBAYARAN]")
        print()
        print("Pilih metode pembayaran yang akan Anda lakukan:")
        print('1. Cash')
        print('2. Debit Card') 
        
        pilih = input("Pilih yang Anda inginkan (1/2):  ")
        if pilih == "1":
            cash = int(input('Uang dari penginap: Rp. '))
            #resepsionis menginputkan uang yang diberikan oleh tamu/penginap
            
            kurang = str(tarif - cash)
            kembali = str(cash - tarif)
            if (cash > tarif):
                print ('Jumlah kembalian adalah :'+ 'Rp.' + str(kembali)+',00-')
                #program akan menampilkan kembalian yang harus diberikan kepada tamu/penginap
                print("""
            Terima kasih telah melakukan reservasi di hotel kami
            Selamat menikmati penginapan yang nyaman
            Semoga hari Anda menyenangkan:)
            """)
            
            else:
                print ('Maaf uang Anda kurang sebesar :'+ 'Rp.' + str(kurang)+',00-')
                #program akan menampilkan kekurangan uang yang harus dibayarkan lagi oleh tamu/penginap
                os.sys('cls')
                print('Pastikan uang anda cukup')
                continue


        else:
            saldo = input('Apakah saldo mencukupi? [y/n]: ')
            if saldo == 'y':
            #respsionis akan mengambil kartu debit dari tamu/penginap
            #jika kartu debit dapat digunakan (saldo cukup) , resepsionis akan menginputkan 'y'
                print("""
                Terima kasih telah melakukan reservasi di hotel kami
                Selamat menikmati penginapan yang nyaman
                Semoga hari Anda menyenangkan:)
                """)
            else :
            #respsionis akan mengambil kartu debit dari tamu/penginap
            #jika kartu debit tidak dapat digunakan (saldo tidak cukup) , resepsionis akan menginputkan 'n'
                print ("""
                Mohon maaf sisa saldo Anda tidak mencukupi untuk melakukan reservasi ini.
                Silahkan gunakan debit card lain atau menggunakan metode pembayaran lain
                """)
                ubah = input ('Ingin mengubah metode pembayaran atau mengganti debit card? [y/n]: ')
                #tamu/penginap dapat mengubah metode pembayaran / mengganti karti debit
                if ubah == 'y':
                    change = input('Ubah metode pembayaran menjadi cash? [y/n]: ')
                    #menawarkan tamu/penginap untuk mengubah pembayaran menjadi cash
                    if change == 'y':
                        os.sys('cls')
                        continue
                    else :
                        ganti = input ('Ingin mengganti debit card? [y/n]: ')
                        #menawarkan tamu untuk mengganti debit card
                        if ganti == 'y':
                            saldo = input('Apakah saldo mencukupi? [y/n]: ')
                            if saldo == 'y':
                                print("""
                                Terima kasih telah melakukan reservasi di hotel kami
                                Selamat menikmati penginapan yang nyaman
                                Semoga hari Anda menyenangkan:)
                                """)
                            else:
                                os.sys('cls')
                                print('Gunakan pembayaran Cash saja')
                                #ketika kartu debit tamu/penginap yang ke 2 masih tetap kurang saldonya
                                #tamu/penginap akan disarankan untuk menggunakan metode cash saja
                        else :
                            os.sys('cls')
                else :
                    
                    sys.exit()
                    
        ulang =''
        while ulang!= 'y' and ulang!= 't':
            #resepsionis akan menanyakan kembali kepada tamu/penginap ,
            ulang = input('Apakah anda ingin memesan kamar lagi [y/t] : ')
            if ulang == 'y':
                os.system('cls')
                print ('Silahkan pilih lagi')
                #ketika ingin memesan lagi, program akan mengulang dari awal
            elif ulang =='t':
                print('Terimakasih telah melakukan reservasi di Hotel kami :)')
                sys.exit()
            #program selesai


exit()
   




