jawab="y"
while jawab == "Y" or jawab=="y":

    print("===============")
    print('CEK KELULUSAN')
    print('===============')
    n = input('MASUKKAN NILAI = ')
    if int(n)>60:
        status = "LULUS"
    else:
        status="TIDAK LULUS"
    print("STATUS = %s"%status)

    jawab = input("CEK LAGI? (Y/T) = ")
    if jawab =="T" or jawab=="t":
       break