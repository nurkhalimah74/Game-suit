print ('\n" Perhitungan BB Ideal dengan Rumus BMI "')
user = input ("Haiiiii :) \nSiapa namamu ? ")
bb = int (input ("Berapa kg berat badanmu ? "))
tb = float (input ("Berapa m tinggi badanmu ? "))

bbi = (bb / (tb*tb))
if bbi < 18.5:
    print ("\nyahhh :( \nberat badanmu kurang ", user)
elif bbi >= 18.5 and bbi <= 22.9:
    print ("\nYeayyyy ! berat badanmu normal ", user)
else:
    print ("\nHAAAAA :( \nberat badanmu berlebih ", user)    