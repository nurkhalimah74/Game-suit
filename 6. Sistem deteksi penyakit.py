print ("+-------------------------------------------------------+")
print ("|\tSelamat Datang di Aplikasi Sistem Pakar\t\t|")
print ("|\t   Deteksi Malaria & Demam Berdarah \t\t|")
print ("+-------------------------------------------------------+")

nama = input ("Nama\t: ")
pil = input ("Hai " + nama + ", \nApakah anda ingin melakukan Diagnosa ?  (Ya / Tidak) : ")

while pil == "Ya" :
    print ("\nApakah anda merasakan gejala berikut ini ?")
    print ("1. Demam / suhu badan tinggi")
    print ("2. Sakit kepala")
    print ("3. Nyeri pada sendi, otot, dan tulang")
    print ("4. Mual dan muntah")
    diag1 = input ("Jawab (Ya / Tidak) : ")
    
    if diag1 == "Ya" :
        print ("\nApakah anda juga merasakan gejala berikut ini ? ")
        print ("1. Hilang nafsu makan")
        print ("2. Nyeri pada bagian belakang mata")
        print ("3. Ruam kemerahan")
        diag2 = input ("Jawab (Ya / Tidak) : ")
        
        if diag2 == "Ya" :
            print ("\nHi, " + nama + " hasil awal diagnosa kamu adalah : ")
            print ("Gejala demam berderah, segera ke dokter yaaa ")
        elif diag2 == "Tidak" :
            print ("\nApakah anda juga merasakan gejala berikut ini ? ")
            print ("1. Menggigil sedang sampai berat")
            print ("2. Tubuh kelelahan")
            print ("3. Banyak berkeringat")
            print ("4. Diare")
            diag3 = input ("Jawab (Ya / Tidak) : ")
            
            if diag3 == "Ya" :
                print ("\nHi, " + nama + " hasil awal diagnosa kamu adalah :" )
                print ("Gejala malaria, segera ke dokter yaaa")
            elif diag3 == "Tidak" :
                print ("\nHi, " + nama + " sepertinya anda sedang banyak hutang")
                
            else :
                print("\nHi, " + nama + " sepertinya anda tidak mau berobat")
        else :
                print("\nHi, " + nama + " sepertinya anda tidak mau berobat")        
                
    elif diag1 == "Tidak" :
        print ("\nHi, " + nama + " sepertinya anda butuh jalan-jalan hehehee")
    else :
        print("\nHi, " + nama + " sepertinya anda tidak mau berobat")
 
               
    print ("\n+-------------------------------------------------------+")
    pil = input ("Hai " + nama + ", \nApakah anda ingin melakukan Diagnosa ?  (Ya / Tidak) ")

    if pil == "Ya" : 
        print ("+-------------------------------------------------------+")
        print ("|\tSelamat Datang di Aplikasi Sistem Pakar\t\t|")
        print ("|\t   Deteksi Malaria & Demam Berdarah \t\t|")
        print ("+-------------------------------------------------------+")
    else :
        print ("\n+-------------------Terima kasih---------------------+")

            
            
            
            
            
            
            
            
            
            
            
