angka =  float(input("Masukkan Angka yang Anda Inginkan : \n"))

if angka % 2 == 0 :
    print("Angka yang anda masukkan merupakan Bilangan Genap Yaitu %s" % angka)
elif angka % 2 == 1 :
    print("Angka yang anda masukkan merupakan Bilangan Ganjil Yaitu %s" % angka)
else :
    print("Angka yang anda masukkan bukan Bilangan Bulat yaitu %s" % angka)

