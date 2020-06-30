# tipe data skalar => sederhana
anak1 = 'eko'
anak2 = 'dwi'
anak3 = 'tri'
anak4 = 'catur'

print(anak1)
print(anak2)
print(anak3)
print(anak4)

# tipe data list/daftar/array

anak = ['eko', 'Dwi', 'Tri', 'Catur']
print(anak)
anak.append('panca')
print(anak)

#sapa anak ke2
print(f'hai {anak[1]}')

#sapa semua anak
nama_anak: str
for nama_anak in anak :
    print(f' hai {nama_anak}')

for a in range (0,len(anak)):
    print (f'hai{anak[a]}')