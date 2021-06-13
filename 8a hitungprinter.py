jawab="y"
while jawab=="Y" or jawab=="y":

    print("===================")
    print("TRANSAKSI PEMBELIAN")
    print("===================")

    hrg="660000"
    n = int(input("JUMLAH PRINTER= "))
    total = int(hrg)*int(n)
    print("TOTAL BAYAR = Rp. %s"%total)

    jawab = input("TAMPILKAN LAGI? (Y/T) =")
    if jawab=="T" or jawab=="t":
        break