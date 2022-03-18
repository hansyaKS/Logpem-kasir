import datetime
import numpy as np

# salutation
print("ini adalah program kasir\nsilahkan dipilih")
# global variable
selesai="n"
total = []
hargaTotal= []


#list of item with atribute name and price
class item:
    # x=["keju","daging","saus","babi","tempe","tahu","pecel","ayam", "cilok","cireng","telur","kentang"]
    # x_price=[2, 6, 8, 7, 9, 8, 5, 4, 3, 6, 1, 2]
    f= np.loadtxt("save.txt", dtype=str,delimiter=",")

    x=f[:,0]
    x_price=f[:,0]

#function

        
def printlist():
    # print list of item to be selected by 
    print()
    for i in range(0, 15):
        for j in range(0+i,len(item.x),15):
            print(j+1,") ",item.x[j],'\t harga=',item.x_price[j],"\t",end="")
        print()

def printtotal():
    a= list(set(total))
    b=[]
    # sorting item name in list a to match the price at item.x_price
    for i in range(0, len(a)):
        check=a[i]
        for j in range(0,len(item.x)):
            if check==item.x[j]:
                b.append(item.x_price[j])

    # printing list of item to buy, its price and total price
    print("\n            Hal yang Dipilih             \nitem\tharga\tjumlah\t jumlahtotal")
   
    for i in range(0,len(a)):
        print(a[i],"\t|",b[i], "\t|", total.count(a[i]),
        "\t|",b[i]*total.count(a[i]))
    print ("\nharga total=\t",sum(hargaTotal),".000")


def struckconstruct():
    print("\n\n\n\tStruk Pembayaran\nSistem pemesanan makananan LOGPEM B\n\nDate and time :",datetime.datetime.now() )
    printtotal()
    print("\nTerimakasih sudah melakukan transaksi\nkami tunggu kedatangan anda kembali\n\nlayanan pengaduan : hansa@mail.ugm.ac.id")
    # print(datetime.datetime.now())



# ****mainloop*******
  
# interface for selecting item 
while selesai != "y":
    printlist()
    #user inputing corespondent item then convert into list
    masukanLi= list(map(int,input("\nmasukkan angka \t:").strip().split()))
    #storing list of item to buy to total and hargaTotal variable
    for i in range(0,len(masukanLi)):
        masukan= masukanLi[i]
        for j in range(0,len(item.x)):
            if masukan ==int(j+1):
                total.append(item.x[j])
                hargaTotal.append(item.x_price[j])

    # checking order prompt
    printtotal()
    # selesai= str (input("\n apakah anda sudah selesai memilih? (y/n)\t: "))
    if input("\n apakah anda sudah selesai memilih? (y/n)\t: ")=="n":   
        #reset buylist prompt
        if input("apakah mau reset (y/n)\t: ")== "y":
            total = []
            hargaTotal=[]
    else:
        selesai="y"

struckconstruct()
# printtotal()

# print(*total, sep=", ")