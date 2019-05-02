#!/usr/bin/env python
# coding: utf-8

# In[10]:


class Kubus:
    def __init__(self,s):
        self.sisi = s
    def tampilkansisi(self):
        print(self.sisi)
    def luas(self):
        print("Luas : ",self.sisi**2)
    def luaspermukaan(self):
        print("Luas permukaan :",self.sisi**2*6)
    def volume(self):
        print("volume :",self.sisi**3)

kubus1 = Kubus(4)
kubus1.tampilkansisi()
kubus1.luas()
kubus1.luaspermukaan()
kubus1.volume()


# In[11]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year

class Pegawai:
    def __init__(self,n,j,g,lahir):
        self.nama = n
        self.jabatan = j
        self.gaji = g
        self.tahunlahir = lahir
    def tampilkan(self):
        print(self.nama,",",self.jabatan,",",self.gaji*30)
    def tampilkanumur(self):
        print("Umur :",tahun - self.tahunlahir)
        
p1 = Pegawai("m.fahriz zain jannan","Direktur",500000,2000)
p1.tampilkan()
p1.tampilkanumur()


# In[3]:


class Mahasiswa:
    def __init__(self,n,no,ip):
        self.nama = n
        self.nim = no
        self.ipk = ip
    def ceklayak(self):
        if(self.ipk<3):
            print(self.nama,"tidak layak bidikmisi")
        else:
            print("Anda layak Bidikmisi")
    def datamhs(self):
        print(self.nama,",",self.nim,",",self.ipk)
        
m1 = Mahasiswa("M.fahriz zain jannan","180441100075",2.75)
m1.datamhs()
m1.ceklayak()
m2 = Mahasiswa("Siapa dia?","180441100030",3.5)
m2.datamhs()
m2.ceklayak()
print(m1==m2)


# In[1]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class pegawai:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th
    def user(self):
        print("nama",self.nama,"nim",self.nim)
    def prediksi_umur(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

pg1 = pegawai("zein","180441100075","pamekasan",8,6,2000)
pg1.user()
pg1.prediksi_umur()


# In[5]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class orang:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th

    def perkenalkan_anda(self):
        print("hello,saya", self.nama,"Nim",self.nim,"lahir_di",self.tempat_lahir,self.tanggal_lahir,self.bulan_lahir,self.tahun_lahir)
    def prediksi_umur(self):
        print("prediksi_Umur :",tahun - self.tahun_lahir,"")
    def umur_sekarang(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

org1 = orang("zein","180441100075","pamekasan",8,6,2000)
org1.perkenalkan_anda()
org1.prediksi_umur()
org1.umur_sekarang()


# In[2]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month

class Mahasiswa:
    def __init__(self,nim,nm):
        self.npm = nim
        self.nama = nm
    def perkiraan_semester(self):
        self.angkatan = "20"+self.npm[:2]
        self.angkatan = int(self.angkatan)
        self.smt = tahun - self.angkatan
        if(bulan>=2 and bulan<=7):
            if(self.smt ==1):
                self.semester = "semester 2"
            elif(self.smt ==2):
                self.semester = "semester 4"
            elif(self.smt ==3):
                self.semester = "semester 6"
            elif(self.smt ==4):
                self.semester = "semester 8"
            else:
                self.semester = "semester tua"
        if(bulan<2 and bulan>7):
            if(self.smt ==1):
                self.semester = "semester 1"
            elif(self.smt ==2):
                self.semester = "semester 3"
            elif(self.smt ==3):
                self.semester = "semester 5"
            elif(self.smt ==4):
                self.semester = "semester 7"
            else:
                self.semester = "semester tua"
    def hasil(self):
        print("nama : ",self.nama)
        print("nim : ",self.npm)
        print("Sekarang : ",self.semester,"\n")

m1 = Mahasiswa("180441100075","zein")
m1.perkiraan_semester()
m1.hasil()

m2=Mahasiswa("160441100075","tama")
m2.perkiraan_semester()
m2.hasil()

m3=Mahasiswa("180441100065","galih")
m3.perkiraan_semester()
m3.hasil()


# In[3]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class mahasiswa:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th

    def perkenalan_saya(self):
        print("hello,saya", self.nama,"Nim",self.nim,"lahir_di",self.tempat_lahir,self.tanggal_lahir,self.bulan_lahir,self.tahun_lahir)
    def umur_sekarang(self):
        print("preiksi_Umur :",tahun - self.tahun_lahir)
    def prediksi_umur(self):
        print("umur_saya :",tahun - self.tahun_lahir,"tahun",bulan - self.bulan_lahir,"bulan",hari - self.tanggal_lahir,"hari")
mhs1 = mahasiswa("zein","180441100075","pamekasan",8,6,2000)
mhs1.perkenalan_saya()
mhs1.umur_sekarang()
mhs1.prediksi_umur()


# In[4]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class orang:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th

    def perkenalkan_anda(self):
        print("hello,saya", self.nama,"Nim",self.nim,"lahir_di",self.tempat_lahir,self.tanggal_lahir,self.bulan_lahir,self.tahun_lahir)
    def umur_sekarang(self):
        print("preiksi_Umur :",tahun - self.tahun_lahir)
    def prediksi_umur(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

org1 = orang("zein","180441100075","pamekasan",8,6,2000)
org1.perkenalkan_anda()
org1.umur_sekarang()
org1.prediksi_umur()


# In[5]:


from datetime import datetime
sekarang = datetime.now()
tahun = sekarang.year
bulan = sekarang.month
hari = sekarang.day

class pegawai:
    def __init__(self, n, no, tl ,tg,bln, th):
        self.nama = n
        self.nim = no
        self.tempat_lahir = tl
        self.tanggal_lahir=tg
        self.bulan_lahir=bln
        self.tahun_lahir=th
    def user(self):
        print("nama",self.nama,"nim",self.nim)
    def prediksi_umur(self):
        self.usia=tahun-self.tahun_lahir
        if(self.bulan_lahir==bulan):
            if(self.tanggal_lahir>hari):
                self.usia=self.usia-1
        elif(self.bulan_lahir>bulan):
                self.usia=self.usia-1
        print("umur_sekarang",self.usia,"tahun")

pg1 = pegawai("zein","180441100075","pamekasan",8,6,2000)
pg1.user()
pg1.prediksi_umur()


# In[6]:


class shark():
    def swim(self):
        print("the shark is swim")
    def swim_backwards(self):
        print("the shark cannot swim backwars,but can sink backward")
    def skalaton(self):
        print("the shark skelaton is mode of cartilago")

class clamfish():
    def swim(self):
        print("the clam fish is swim")
    def swim_backwards(self):
        print("the clamfish can swim backwars,but can sink backward")
    def skalaton(self):
        print("the clamfish skelaton is mode of bone")
abc=shark()
abc.skalaton()

easy=clamfish()
easy.skalaton()

for fish in(abc,easy):
    fish.swim()
    fish.swim_backwards()
    fish.skalaton()


# In[7]:


class shark():
    def swim(self):
        print("the shark is swim")
    def swim_backwards(self):
        print("the shark cannot swim backwars,but can sink backward")
    def skalaton(self):
        print("the shark skelaton is mode of cartilago")

class clamfish():
    def swim(self):
        print("the clam fish is swim")
    def swim_backwards(self):
        print("the clamfish can swim backwars,but can sink backward")
    def skalaton(self):
        print("the clamfish skelaton is mode of bone")
abc=shark()
abc.skalaton()

easy=clamfish()
easy.skalaton()


# In[8]:


class user:
    def __init__(self,n):
        self._first_name=n
    def p(self):
        print ("hello",self._first_name)
class programer(user):
    def __init__(self,n,last):
        user.__init__(self,n)
        self.last_name=last
    def P(self):
        print ("hello",self._first_name+" "+self.last_name)
brian=programer("zein","baim")
brian.P()


# In[9]:


class binatanng:
    def __init__(self,nama):
        self.nama=nama
    def cara_berjalan(self):
        raise  NotImplementedError("sub class must implemented abstrak metho")
class kucing(binatanng):
    def cara_berjalan(self):
        return "berjalan merangkak"
    def bersuara(self):
        return "meong"
class anjing (binatanng):
    def cara_berjalan(self):
        return "berjalan merangkak"
    def bersuara(self):
        return  "gog"
class ular (binatanng):
    def cara_berjalan(self):
        return "merayap"
    def bersuara(self):
        return "essst"
binatanng=[anjing('bull'),
           kucing('anggora'),
           ular('cobra')]
for binatanng in binatanng:
    print(binatanng.nama,":",binatanng.bersuara(),":",binatanng.cara_berjalan())


# In[ ]:


Encapsulation an operator overlooing


# In[2]:


class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    #def __str__(self):
        #return "({0},{1})".format(self.x,self.y)
    def __str__(self):
        return "Point object is at:("+str(self.x)+","+str(self.y)+")"
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x,y)
    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)
    
p1 = Point(2,3)
p2 = Point(-1,2)
print(p1-p2)
print(p1+p2)


# In[3]:


class Fraction:
    def __init__(self,top,bottom):
        self.atas = top
        self.bawah = bottom
    
    #def show(self):
        #print(self.num,"/",self.den)
        
    def __str__(self):
        return str(self.atas)+"/"+str(self.bawah)


    def __add__(self,other):
        newatas = self.atas * other.bawah + self.bawah * other.atas
        newbawah = self.bawah * other.bawah
        return Fraction(newatas,newbawah)
    
    def __sub__(self,other):
        newatas = self.atas * other.bawah- self.bawah * other.atas
        newbawah = self.bawah* other.bawah
        return Fraction(newatas,newbawah)
    
    def __truediv__(self,other):
        newatas = self.atas* other.bawah
        newbawah = self.bawah * other.atas
        return Fraction(newatas,newbawah)

    def __mul__(self, other):
        newatas = self.atas * other.atas
        newbawah = self.bawah * other.bawah
        return Fraction(newatas,newbawah)
    
f=Fraction(2,4)
#Show(f)
print(f)
f1 = Fraction(1,4)
f2 = Fraction(1,2)
print("hasil tambah pecaha :",f1+f2)
print("hasil kurang pecahan :",f1-f2)
print("hasil bagi pecahan :",f1/f2)
print("hasil kali pecahan :",f1*f2)


# In[4]:


#encapsulation
class robot(object):
    def __init__(self):
        self.__version=22
    def getversion(self):
        print(self.__version)
    def setversion(self,version):
        self.__version=version
obj=robot()
obj.getversion()
obj.setversion(23)
obj.getversion()
#print(obj.__version) salah karena tdk ada pemanggilan classs
print(obj._robot__version)


# In[5]:


class A(object):
    #public method
    def myPublicMethod(self):
        return "This is a public method"
    #private method with single underscore
    def _myPrivateMethod(self):
        return "This is a private method"
    #private method with double underscore
    def __myAnotherPrivateMethod(self):
        return "This is another private method"
#nama objek
obj1 = A()
#we can access the public mehod which is cool
print(obj1.myPublicMethod())
#Note that we can also access the private method from outside
print(obj1._myPrivateMethod())
print(obj1._A__myAnotherPrivateMethod())


# In[6]:


class Car:
 
    __maxspeed = 0
    __name = ""
 
    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"
 
    def drive(self):
        print ("driving. maxspeed : " + str(self.__maxspeed))
 
redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar._Car__maxspeed=10 #cara mengubah variabel private
redcar.drive()


# In[7]:


class Car:
 
    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print ('driving')

    def __updateSoftware(self):
        print ('updating software')
 
redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object.


# In[8]:


class Shape(object):
    __nama = 0
    def getNama(self):
        print ("Nama:",self.__nama)
    def setNama(self,nama):
        self.__nama = nama
    
class Rectangle(Shape):
    __panjang = 0
    __lebar = 0
    def getPanjangdanLebar(self):
        print ("Panjang:",self.__panjang)
        print ("Lebar:",self.__lebar)
    def setPanjangdanLebar(self,panjang,lebar):
        self.__panjang = panjang
        self.__lebar = lebar

class Circle(Shape):
    __jari2 = 0
    def getJari2(self):
        print ("Jari-jari:",self.__jari2)
    def setJari2(self,jari2):
        self.__jari2 = jari2

class Triangle(Shape):
    __panjang = 0
    __sisi = 0
    def getPanjangdanSisi(self):
        print ("Panjang:",self.__panjang)
        print ("Sisi:",self.__sisi)
    def setPanjangdanSisi(self,panjang,sisi):
        self.__panjang = panjang
        self.__sisi = sisi
Segitiga = Triangle()
Segitiga.setNama ("Segitiga Sama Sisi")
Segitiga.setPanjangdanSisi(5,75)
Segitiga.getNama ()
Segitiga.getPanjangdanSisi ()

Persegipanjang = Rectangle ()
Persegipanjang.setNama ("Persegi Panjang")
Persegipanjang.setPanjangdanLebar (10,15)
Persegipanjang.getNama ()
Persegipanjang.getPanjangdanLebar ()

Lingkaran = Circle ()
Lingkaran.setNama ("Lingkaran besar")
Lingkaran.setJari2 (21)
Lingkaran.getNama ()
Lingkaran.getJari2 ()


# In[9]:


class bilangan:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,other):
        return self.a+other.a,self.b+other.b
    def __sub__(self,other):
        return self.a-other.a,self.b-other.b
    def __str__(self):
        return self.a,self.b
o1=bilangan(52,3)
o2=bilangan(6,7)
o3=o1+o2
o4=o1-o2
print (o3)


# In[ ]:




