def segitiga() :
    n = 1
    m = 15

    for i in range(m) :
        if n <= m and n % 2 == 1 :
                bentuk = "*"*n
                print(bentuk.center(m))
                n += 1
                continue
        elif n <= m and n % 2 == 0 :
            n += 1
            continue
        else :
            break

segitiga()

Print('##  Program Python Persegi Bintang  ##')
Print('======================================')
Print()
 
besar_persegi = int(input('Input besar persegi: '))
Print()
 
for i in range(besar_persegi):
  for j in range(besar_persegi):
    Print(' *',end='')
Print()