# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 19:44:46 2021

@author: DWI PRAMONO
"""

#Buat program untuk menampilakan dan menghitung biaya total Bengkel UD. Matahari
#1. set variabel merk, jumlah, harga, subtotawal, subtotakhir, diskon, ppn, total
#2. input pilihan merk oli dan harga
#3. input jumlah
#4. subtotawal = harga * jumlah
#5. jika subtotalawal > 200000 maka mendapat diskon 5%
#6. diskon = subtotalawal * 0.05
#7. subtotakhir = subtotawal - diskon
#8. semua transaksi dikenakan ppn 1%
#10. ppn = subtotakhir * 0.01
#11. total = subtotakhir - ppn
#12. tampilkan merk, harga, subtotakhir, diskon, ppn, total

ulang = "y"
while ulang=="y" or ulang=="Y":
    
    print ("===========================================")
    print ("        BENGKEL MOTOR UD. MATAHARI ")
    print ("===========================================")
    print ("")
    print ("               List Merk Oli")
    print ("-------------------------------------------")
    print (" A. Duration SW20 1L")
    print (" B. Castrol Magnatec 1L")
    print (" C. Federal Supreme XX 1L")
    print (" D. Yamalube 1L")
    print (" E. Shell 1L")
    print ("-------------------------------------------")
    
    merk = ['Duration SW20 1L','Castrol Magnatec 1L','Federal Supreme XX 1L','Yamalube 1L','Shell 1L','-']
    harga = [53000,50000,54000,45000,46000,0]
    
    pilihan = input(" Masukkan list abjad Merk Oli = ")
    print ("-------------------------------------------")
    
    #identifikasi pilihan
    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    elif pilihan=="c":
        idx = 2
    elif pilihan=="d":
        idx = 3
    elif pilihan=="e":
        idx = 4
    else:
        idx = 5
        pesan = "   !!! Masukkan Sesuai List yang ada !!!"
        print (pesan)
        print("")
    jumlah = int(input(" Jumlah     = "))
        
    #cetak tampilan layar
    print(" Merk Oli   = " + merk[idx])
    print(" Harga      = Rp." + str(harga[idx]))
    
    #hitung transksi
    fixharga = harga[idx]
    subtotawal = fixharga * jumlah
    if subtotawal > 200000:
        diskon = subtotawal * 0.05
    else:
        diskon = 0
    subtotakhir = subtotawal - diskon
    ppn = subtotakhir * 0.01
    total = subtotakhir - ppn
    print(" diskon     = Rp." + str(diskon))   
    
    #tampilkan total ongkir
    print("-------------------------------------------")
    print(" Subtotal   = Rp." + str(subtotakhir))
    print('-------------------------------------------')
    print("")
    print(" PPN        = Rp." + str(ppn))
    print("")
    print("-------------------------------------------")
    print(" TOTAL      = Rp." + str(total))
    print("")
    print("===========================================")
    print("               TERIMA KASIH")
    print("===========================================")

    jawab = input (" ULANGI PROGRAM ? Y/T = ")
    if jawab == "t" or jawab =="T":
        break