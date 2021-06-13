jawab="y"
while jawab=="Y" or jawab=="y":

    print("==================")
    print("PENILAIAN HURUF")
    print("==================")

    n = input("MASUKKAN NILAI=")

    if int(n)>0 and int(n)<=100:
        if int(n)>=91:
            sts="A"
        elif int(n)>=81: sts="B"
        elif int(n)>=71: sts="C"
        else:
            sts="D"
        print("STATUS = %s"%sts)
    
    else:
        pesan="MASUKKAN NILAI 0-100"
        print(pesan)

    jawab = input("TAMPILKAN LAGI? (Y/T) =")
    if jawab=="T" or jawab=="t":
        break