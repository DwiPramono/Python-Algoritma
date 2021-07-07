import datetime

ulang="y"
while ulang=="y" or ulang=="Y":
    
    print("------------------------------------------")
    print("               SLIP GAJI")
    print("  Tanggal: " + str(datetime.datetime.now()))
    print("------------------------------------------")
    print("")
    
    
    nama        = input("Masukan Nama        = ")
    golongan    = input("Masukan GOLONGAN    = ")
    gender      = input("Jenis Kelamin (L/P) = ")
    kawin       = input("Status Kawin  (K/B) = ")
    
    if golongan=="1":
        gapok = 2500000
    elif golongan=="2":
        gapok = 4500000
    elif golongan=="3":
        gapok = 6500000
        
    print("")    
    print("Gaji Pokok          = Rp. " + str(gapok))
    print("")
    
    if gender=="L" or gender=="l" and kawin=="K" or kawin=="k":
        if golongan=="1":
            tuntri=2500000 * 0.01
        elif golongan=="2":
            tuntri=4500000 * 0.03
        else:
            tuntri=6500000 * 0.05
    elif kawin=="B" or kawin=="b":
        tuntri=0
    
    print("Tunjangan Istri     = Rp. " + str(tuntri))
    print("")
    
    if kawin=="K" or kawin=="k":
        if golongan=="1":
            tunak=2500000 * 0.02
        elif golongan=="2":
            tunak=4500000 * 0.02
        else:
            tunak=6500000 * 0.02
    else:
        tunak=0
    
    print("Tunjangan Anak      = Rp. " + str(tunak))
    print("")
    
    gabru = gapok + tuntri + tunak
    
    print("Gaji Bruto          = Rp. " + str(gabru))
    print("")
    
    jabatan = 0.005 * gabru
    
    print("Biaya Jabatan       = Rp. " + str(jabatan))
    print("")
    
    pensiun = 15500
    
    print("Iuran Pensiun       = Rp. " + str(pensiun))
    print("")
    
    organisasi = 3500
    
    print("Iuran Organisasi    = Rp. " + str(organisasi))
    print("")
    
    netto = gabru - jabatan - pensiun - organisasi
    
    print("Gaji Netto          = Rp. " + str(netto))
    print("")
    print("--------------------------------------------")
    
    jawab = input("Hitung Lagi ? Y/T = ")
    if jawab == "t" or jawab == "T":
        break