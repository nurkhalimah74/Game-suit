print ('\n" Perhitungan BB Ideal dengan Rumus Broca "')
user = input ("Haiiiii :) \nSiapa namamu ? ")
tb = int (input ("Berapa cm tinggi badanmu ? "))

bbp = ((tb-100) - ((tb-100)*15/100))
bbl = ((tb-100) - ((tb-100)*10/100))

print ("\nPilih yaaa :")
print ("1. Perempuan")
print ("2. Laki-laki")
pl = int (input ("kamu 1 atau 2 ? "))
if pl == 1:
    print ('\n', user, ", berat badan idealmu adalah ", bbp, 'kg')
if pl == 2:
    print ('\n', user, ", berat badan idealmu adalah ", bbl, 'kg')  