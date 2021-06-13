jawab="y"
while jawab=="Y" or jawab=="y":

    print("===================")
    print("TRANSAKSI PEMBELIAN")
    print("===================")

    hrg="660000"
    n = int(input("JUMLAH PRINTER= "))
    total = int(hrg)*int(n)
    if int(total)>1500000:
        tothrg = int(total)*0.15
    else:
        tothrg=0
    totakhir = int(total)-int(tothrg)
    print("TOTAL BAYAR = Rp. %s"%totakhir)

    jawab = input("TAMPILKAN LAGI? (Y/T) =")
    if jawab=="T" or jawab=="t":
        break