angka = int(input('\x1b[1;93mMasukkan angka: '))
print("\x1b[0m")
print('\x1b[1;92m=============================================\x1b[0m')
print('\x1b[1;92m|\x1b[0m          \x1b[1;93mMASUKKAN PILIHAN ANDA:\x1b[0m           \x1b[1;92m|\x1b[0m')
print('\x1b[1;92m|\x1b[0m 1.Menentukan bilangan positif dan negatif \x1b[1;92m|\x1b[0m')
print('\x1b[1;92m|\x1b[0m 2.Menentukan bilangan genap dan ganjil    \x1b[1;92m|\x1b[0m')
print('\x1b[1;92m=============================================\x1b[0m')
print('')
pilih = int(input('\x1b[1;93mMasukkan pilihan anda: '))
if pilih ==1:
    print('')
    print('\x1b[1;92mMENENTUKAN BILANGAN POSITIF DAN NEGATIF\x1b[0m')
    print('')
    if angka >0:
        print('Angka \x1b[1;94m'+str(angka)+'\x1b[0m adalah bilangan \x1b[1;94mpositif\x1b[0m')
        print('')
    elif angka >0:
        print('Angka \x1b[1;94m'+str(angka)+'\x1b[0m adalah bilangan \x1b[1;91mpositif\x1b[0m')
        print('')
    else:
         print('Angka yang anda masukkan adalah \x1b[1;94m'+str(angka)+'\x1b[0m')
         print('')
elif pilih ==2:
    print('')
    print('\x1b[1;92mMENENTUKAN BILANGAN GENAP DAN GANJIL\x1b[0m')
    print('')
    if angka % 2 == 0:
        print('Angka \x1b[1;94m'+str(angka)+'\x1b[0m adalah bilangan \x1b[1;94mGenap\x1b[0m')
        print('')
    else:
        print('Angka \x1b[1;94m'+str(angka)+'\x1b[0m adalah bilangan \x1b[1;91mGanjil\x1b[0m')
        print('')
else:
    print('')
    print('\x1b[1;91mPilihan yang anda masukkan tidak tersedia.\x1b[0m')