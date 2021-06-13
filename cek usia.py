jawab="y"
while jawab == "Y" or jawab=="y":

    print("==================")
    print("CEK GOLONGAN USIA")
    print("==================")

    u = input("MASUKKAN USIA = ")

    if int(u)>0 and int(u)<=100:
        if int(u)>=60:
            status="LANSIA"
        elif int(u)>=35: status="DEWASA"
        elif int(u)>=18: status="PEMUDA"
        elif int(u)>=15: status="REMAJA"
        else:
            status="ANAK"
        print("STATUS = %s"%status)
    else:
        pesan="MASUKKAN USIA 0-100"
        print(pesan)

    jawab = input("CEK LAGI? (Y/T) = ")
    if jawab =="T" or jawab=="t":
        break