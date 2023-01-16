#tugas 1
#contoh hasil nilai latihan

#siswa 1- 50,60,80,65
#siswa 2- 70 55 80
#siswa 3- 66,45,35,67
#siswa 4- 80,90,77,75

nilai = [[50,60,80,65],[70,55,80],[66,45,35,67],[80,90,77,75]]

print(nilai[0])
print(nilai[2])
print(nilai[0] [2])
print(nilai[2] [0])

#tugas 2
#deklarasi array
array = []
#membuat deklarasi total
total = 0
n = int(input("masukan jumlah element array : "))
for x in range(n) :
    nilai = float(input("masukan nilai ke- {} :".format(x+1)))
    array.append(nilai)
    #menjumlahkan jumlah dari nilai ;
    print("\n hasil nilai total adalah : {} ".format(sum(array)))
    print("\n hasil rata rata adalah : {} ".format(sum(array)))

#tugas 3
#rom array import *

#nuat variable array i yang, masukan, nilai array
nilai = array('b',[1,2,3,4,5])
#menampilkan array

for n  in nilai:
    print(nilai)

#tugas 4
a = [21,34,78]
b = ["meja", "kursi", "meja"]
c = [2,78,76,60,90]

print(a)
print(b)
print(c)
print((a)[2])
print((b)[0])
print((c)[1])

#tugas 5
binatang = ["sapi", "kucing", "tikus", "domba",]
for n in binatang :
    print(n)