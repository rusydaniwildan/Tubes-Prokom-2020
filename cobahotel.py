#
#
#
#
#
#




from datetime import datetime, date
import math
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
    print('\t','      Solo baru Surakarta')
    print()
    print('\t',' Hotel bintang 3 dengan keunggulan: ')
    print('\t','           Nyaman')
    print('\t','            Aman')
    print('\t','           Bersih')
    print('\t','            Asri')
    print()
    print('======================================================')
    print('Pilih yang anda inginkan ?')
    print()
    print('1. CHECK IN')
    print('2. keluar program')
    print()
    
#program dimulai

while loop:
    print_menu() #memanggil def menu diatas
    pilihan = int(input('Masukan pilihan [1/2]: '))
    print() 
    os.system('cls') #membersihkan layar dalam shell
    if (pilihan == 1):  #ketika memilih 'checkIn'
        print()
        print('\t','[ ISI BIODATA PENGINAP ]')
        print('--------------------------------')
        print()
        nama = input('Masukkan nama lengkap penginap : ').upper()
        nohp = input('Masukkan No HP penginap : +62 ')
        if len(nohp) != 4 and len (nohp) != 5: 
            # ketika no hp tidak sama dengan 4/5 digit, program akan menolak.
            os.system('cls')
            print('No Hp anda tidak terdaftar')
            continue
        ktp = input ('Apakah anda memiliki kartu identitas ktp/sim (y/n) : ')
        if ktp == 'n':
            sys.exit('\nError : Anda harus memuliki kartu identitas untuk MENGINAP')      
             # penginap/tamu harus memiliki kartu identitas untuk menginap, jika tidak punya, TIDAK boleh menginap.
        elif ktp == 'y':
            kk = input('Masukkan No identitas kartu : ')
            tl = input("Masukkan Tempat lahir anda : ").upper()
            tt = input ('Masukkan tanggal lahir anda : ')
            print()
            os.system('cls')
        else:
            os.system('cls')
            input('\nError : Anda harus memilih antara (y/n)')
            continue
    elif (pilihan == 2):
        exit()
    else:
        print('Pilihan yang anda masukkan salah, silahkan coba lagi')
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

    tipe = int(input('Masukkan Tipe kamar yang anda pilih : '))
    os.system('cls')
    if (tipe == 1):
        kamar = 'Regular'
        tarif = ['150.000','175.000','200.000','225.000','250.000','275.000','300.000']
        #tarif (harga permalam) dalam berbentuk list, yang akan dipanggil.
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
                #format tanggal
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
                #ketika format tanggal yang dimasukkan tidak sesuai, akan memunculkan pesan tersebut.

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut? ")

            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        #untuk menghitung rentang hari tamu menginap.
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            try:
                pass
            except NameError:
                print()            
            sys.exit('\nError : Maksimal hanya menginap 7 hari')
    elif (tipe == 2):
        kamar = 'Deluxe'
        tarif = ['155.000','185.000','205.000','235.000','275.000','285.000','310.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut? ")

            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang andah isi salah')
            continue

    elif (tipe == 3):
        kamar = 'Suite'
        tarif = ['185.000','285.000','305.000','435.000','575.000','885.000','910.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
            while checkout is None:
                tanggal = input("Masukkan tanggal CheckOut? ")
            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang andah isi salah')
            continue

    elif (tipe == 4):
        kamar = 'President suite'
        tarif = ['355.000','485.000','505.000','635.000','775.000','885.000','990.000']
        os.system('cls')
        while checkin is None:
            tanggal = input("Masukkan tanggal CheckIn? ")
            print('(NOTES: MAKSIMAL MENGINAP 7 HARI)')
            try:
                checkin = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")

        while checkout is None:
            tanggal = input("Masukkan tanggal CheckOut? ")

            try:
                checkout = datetime.strptime(tanggal, "%Y %m %d")
            except ValueError:
                print("Harus berformat \"<Tahun> <bulan> <hari>\"")
        waktuMenginap = checkout - checkin
        waktu =(waktuMenginap.days)
        if (waktu==1):
            tarif2=tarif[0]
        elif (waktu==2):
            tarif2=tarif[1]
        elif (waktu==3):
            tarif2=tarif[2]
        elif (waktu==4):
            tarif2=tarif[3]
        elif (waktu==5):
            tarif2=tarif[4]
        elif (waktu==6):
            tarif2=tarif[5]
        elif (waktu==7):
            tarif2=tarif[6]
        else:
            os.system('cls')   
            print('Waktu yang andah isi salah')
            continue

    else:
        print('Pilihan yang anda pilih salah, silahkan coba lagi')
        #ketika resepsionis salah meng inputkan nomor (selain 1-4)
        continue
        
        break
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
    print('\t','No identitas : '+ str(kk))
    print()
    print('\t','TTL : '+ str(tl) + ','+ str(tt))
    print()
    print('\t','Tipe kamar : '+ str(kamar))
    print()
    print('\t','Waktu : '+ str(waktu)+ ' Malam')
    print()
    print('\t','Biaya : '+ 'Rp.' + str(tarif2)+',00-')
    print()
    print('\t','Bayar dengan uang pas')
    print()
    print()
    print('Terimakasih atas kepercayaan yang anda berikan kepada kami, semoga anda senang')
    print()
    print('Mohon maaf apabilan pelayanan kami kurang maksimal.')
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
            print('Silahkan Ulang dari awal, Pastikan Data yang anda isi BENAR')
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
        
        pilih = input("Pilih yang anda inginkan (1/2):  ")
        if pilih == "1":
            cash = int(input('Uang dari penginap: Rp. '))
            #resepsionis menginputkan uang yang diberikan oleh tamu/penginap
            tarif3 = int(input('Biaya hotel: Rp.'))
            #resepsionis menginputkan biaya hotel, sesuai pada kwitansi
            kurang = str(tarif3 - cash)
            kembali = str(cash - tarif3)
            if (cash > tarif3):
                print ('Jumlah kembalian adalah :'+ 'Rp.' + str(kembali)+',00-')
                #program akan menampilkan kembalian yang harus diberikan kepada tamu/penginap
                print("""
            Terima kasih telah melakukan reservasi di hotel kami
            Selamat menikmati penginapan yang nyaman
            Semoga hari Anda menyenangkan:)
            """)
            
            else:
                print ('Maaf uang anda kurang sebesar :'+ 'Rp.' + str(kurang)+',00-')
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
            ulang = input('Apakah anda ingin memesan kamar lagi [Y/T] : ')
            if ulang == 'y':
                os.system('cls')
                print ('Silahkan pilih lagi')
                #ketika ingin memesan lagi, program akan mengulang dari awal
            elif ulang =='t':
                print('Terimakasih telah melakukan reservasi di Hotel kami :)')
                exit()
            #program selesai


exit()
   




