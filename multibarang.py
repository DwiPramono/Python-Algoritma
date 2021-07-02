# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 15:14:23 2021

@author: DWI PRAMONO
"""

ulang = "y"
while ulang=="y" or ulang=="Y":
    
    print ("===========================================")
    print ("      Kantin Fakultas Tek. Informasi ")
    print ("===========================================")
    print ("")
    print ("               Menu Makanan")
    print ("-------------------------------------------")
    print (" A. Nasi Goreng         15.000")
    print (" B. Lontong Goreng      14.900")
    print (" C. Bakso Goreng        12.900")
    print (" D. Rujak Goreng        13.000")
    print (" E. Rujak Bakso         15.000")
    print (" F. Rujak Bakso Pecel   17.000")
    print ("-------------------------------------------")
    print ("")
    print ("              Menu Minuman")
    print ("-------------------------------------------")
    print (" G. Teh Dingin/Hangat/panas 2.500")
    print (" H. Kopi Dingin             5.000")
    print (" I. Kopi Teh Panas          6.500")
    print (" J. Coca Cola Dingin        3.500")
    print (" K. Coca Cola Panas         5.000")
    print ("-------------------------------------------")
    
    kode = ['a','b','c','d','e','f','g','h','i','j','k']
    makanan = ['Nasi Goreng','Lontong Goreng','Bakso Goreng','Rujak Goreng','Rujak Bakso','Rujak Bakso Pecel','Teh Dingin/Hangat/panas','Kopi Dingin','Kopi Teh Panas','Coca Cola Dingin','Coca Cola Panas']
    harga = [15000,14900,12900,13000,15000,17000,2500,5000,6500,3500,5000]
    
    
    tmbah = "y"
    while tmbah == "y" or tmbah == "Y":
        
        pilihan = input("Masukan Kode Pesanan = ")
        qty     = input("Jumlah Pesanan       = ")
    
    
        #jawab = input("Tambah Pesanan ? Y/T = ")
       # if jawab== "T" or jawab== "t":
           # totbyr
        
        i = 0
        while i<len(makanan):
        #jika value pada list kode[i] == pilihan
            if kode[i] == pilihan:
        #ambil nama barang
                nm_brg = makanan[i]
        #ambil harga satuan
                hrgsat = harga[i]
        #jika tidak cocok, lanjut ke i berikutnya
            i+=1
            
        totbyr = hrgsat * int(qty) 
            
        jawab = input("Tambah Pesanan ? Y/T = ")
        if jawab== "T" or jawab== "t":
           totbyr
        uang = input("Jumlah Uang = ")
        kembali= uang - totbyr
        
        print(">>> NAMA BARANG      : " + nm_brg)
        print(">>> HARGA BARANG     : " + str(hrgsat))
        print(">>> JUMLAH BARANG    : " + qty)
        print(("-------------------------------"))
        print(">>> TOTAL BAYAR      : " + str(totbyr))
        print(">>> BAYAR            : " + str(uang))
        print(">>> KEMBALI          : " + str(kembali))
            
    jawabulang = input("ULANGI PROGRAM ? Y/T")
    if jawabulang== "T" or jawabulang== "t":
        break