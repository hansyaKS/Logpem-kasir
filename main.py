


from array import array


print("ini adalah program kasir\nsilahkan dipilih")
# print("silahkan dipilih")
selesai="n"

total = []
hargaTotal= []

class item:
    x=["keju","daging","saus","babi","tempe","tahu","pecel","ayam", "cilok","cireng","telur"]
    x_price=[2, 6, 8, 7, 9, 8, 5, 4, 3, 6, 1]

def printlist():
    for i in range(0,len(item.x)):
        print(i+1,") ",item.x[i],'\t harga=',item.x_price[i])
        
def printlist2():
    print()
    for a in range(0, 10):
        for i in range(0+a,len(item.x),10):
            print(i+1,") ",item.x[i],'\t harga=',item.x_price[i],"\t",end="")
        print()
       

    
def printtotal2():
    a= list(set(total))
    b=[]
    for i in range(0, len(a)):
        check=a[i]
        for c in range(0,len(item.x)):
            if check==item.x[c]:
                b.append(item.x_price[c])
    for i in range(0,len(a)):
        print(a[i],"\tharga: ",b[i], "\t jumlah barang: ", total.count(a[i]),
        "\t jumlah harga: ",b[i]*total.count(a[i]))

def printtotal():
    print({item:total.count(item) for item in total})
    print ("harga total=\t",sum(hargaTotal),".000")

while selesai!="y":
    
    akhir = "n"
    while akhir != "y":
        printlist2()
        masukanLi= list(map(int,input("\nmasukkan angka \t:").strip().split()))

        for i in range(0,len(masukanLi)):
            masukan= masukanLi[i]
            for a in range(0,len(item.x)):
                if masukan ==int(a+1):
                    total.append(item.x[a])
                    hargaTotal.append(item.x_price[a])
        akhir= str (input("\n apakah anda sudah selesai memilih? (y/n)\t:"))
    
    printtotal()
    selesai=input("apakah sudah sesuai  (y/n)")
    if selesai =="n":
        if input("apakah mau reset (y/n)")== "y":
            total = []
            hargaTotal= int()

printtotal2()

# print(*total, sep=", ")