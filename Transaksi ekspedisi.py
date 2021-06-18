# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 12:31:19 2021

@author: DWI PRAMONO
"""

#Buat program untuk menghitung biaya total pengiriman barang di perusahaan Ekspedisi 
#Lorena di Malang
#1. set variabel kota, jarak, ongkirperkm, totongkir
#2. input pilihan kota
#3. jika kota Sby, jarak = 169, ongkirperkm=2500, selain itu
#jika kota Bdg, jarak = 452, ongkirperkm=4000
#4. totongkir = jarak * ongkirperkm
#5. tampilkan kota, totongkir

ulang="y"
while ulang=="y" or ulang=="Y":
    
    print ("=================================")
    print ("  TRANSKASI BIAYA EKSPEDISI ")
    print ("=================================")
    print ("")
    print (" Kode = A. Surabaya")
    print (" Kode = B. Bandung")
    print ("---------------------------------")

    kota = ['Surabaya','Bandung','-']
    jarak = [169,452,0]
    ongkirperkm = [2500,4000,0]

    pilihan = input(" Masukkan Kode Tujuan = ")
    print ("---------------------------------")
    #identifikasi pilihan

    if pilihan=="a":
        idx = 0
    elif pilihan=="b":
        idx = 1
    else:
        idx = 2
        pesan = "!! Masukkan Kode A atau B saja !!"
        print (pesan)
        print("")
        
    #cetak tampilan layar
    print(" Pilihan Tujuan      = " + kota[idx])
    print(" Jarak               = " + str(jarak[idx]) + " km")
    print(" Ongkir per km       = Rp." + str(ongkirperkm[idx]))

    #hitung transksi
    fixjarak = jarak[idx]
    fixongkirkm = ongkirperkm[idx]
    totongkir = fixjarak * fixongkirkm

    #tampilkan total ongkir
    print("---------------------------------")
    print(" Total Biaya         = Rp." + str(totongkir))
    print("")
    print("=================================")
    print("         TERIMA KASIH")
    print("=================================")
    
    jawab = input ("ULANGI PROGRAM ? Y/T = ")
    if jawab == "t" or jawab =="T":
        break