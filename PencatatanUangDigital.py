saldo= 0

def info_saldo () :
    print ('Saldo Anda saat ini Rp. {}'.format(saldo))

def tambah_saldo (jumlah_tambah_saldo):
    global saldo

    print('Saldo awal Anda Rp. {}' .format(saldo))
    saldo = saldo + jumlah_tambah_saldo
    print ('saldo Anda saat ini Rp. {}'.format (saldo))

def ambil_saldo (jumlah_ambil_saldo):
    global saldo

    print('Saldo Anda Rp. {}' .format(saldo))
    saldo = saldo - jumlah_ambil_saldo
    print ('saldo Anda saat ini Rp. {}'.format (saldo))

pilihan = None
jumlah = None

while True :
    print ("----------------------------------------------------")
    print ("========< Aplikasi Pencatatan Uang Digital >========")
    print ("----------------------------------------------------")
    print ("Selamat datang di Pencatatan Uang digital")

    print ("1. Informasi Saldo ")
    print ("2. Tambah Saldo")
    print ("3. Ambil Saldo")
    print ("4. Keluar Aplikasi")

    pilihan= int(input("Silahkan pilih menu : "))
    if pilihan==1 :
        info_saldo()
    elif pilihan==2:
        jumlah = int(input("Silahkan masukan jumlah saldo : "))
        tambah_saldo(jumlah)
    elif pilihan==3:
        jumlah = int(input("Anda mau ambil saldo berapa? : "))
        if jumlah > saldo :
            info_saldo()
            print ("Maaf, saldo Anda tidak cukup")
        elif jumlah < saldo :
            ambil_saldo(jumlah)       
    elif pilihan==4:
        print (" Terimakasih , Semoga hari Anda menyenangkan :) ")
        exit()
