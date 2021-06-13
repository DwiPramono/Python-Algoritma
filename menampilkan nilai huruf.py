jawab="y"
while jawab=="y" or jawab=="Y":
    
    print ("=====================")
    print ("TAMPILKAN NILAI HURUF")
    print ("=====================")

    n = input("MASUKKAN NILAI = ")

    if int(n)>0 and int(n)<=100:
        if int(n)>80:
            sts="BAIK SEKALI"
        elif int(n)>=65: sts="BAIK"
        elif int(n)>=55: sts="CUKUP"
        elif int(n)>=40: sts="KURANG"
        else:
            sts="KURANG SEKALI"
        print ("STATUS = %s"%sts)

    else:
        pesan="MASUKKAN NIALI 0-100"
        print(pesan)

    jawab = input("TAMPILKAN LAGI? (Y/T)=")
    if jawab=="T" or jawab=="t":
       break