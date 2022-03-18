import numpy as np
total=[]
total_price=[]

class item:
    x=["keju","daging","saus","babi","tempe","tahu","pecel","ayam","cilok","cireng","telur","kentang"]
    x_price=[2, 6, 8, 7, 9, 8, 5, 4, 3, 6, 1, 2]


# class item:
#     x=[]
#     x_price=[]
def inputData():
    x=list((input("\nmasukkan nama dan harga contoh(ayam 2 sapi 5) \t:").strip().split()))
    for i in range(0, len(x),2):
        (item.x)=np.append(item.x,x[i])
        (item.x_price)=np.append(item.x_price,x[i+1])


def save(x,y):    
    f=open("tugasBesar/save.txt","w")
    t=zip((x),(y))
    
    with f as my_file:
        for((x),(y)) in t:
            my_file.write("{0},{1}\n".format((x),(y)))
    print('File created')
       
    f.close()

def delete(x):
    # y=(item.x).index(str(x))
    (item.x).remove(x)
    (item.x_price).remove(x)


def read():
    f= np.loadtxt("save.txt", dtype=str,delimiter=",")

    item.x=f[:,0]
    item.x_price=f[:,1]
    print("\n no\t item \t harga")
    for i in range(0,len(item.x)):
        print(i+1,")",item.x[i],"\t",item.x_price[i])



save(item.x,item.x_price)

end="n"
while(end=="n"):
    y=(input("\tpilihan anda\n1) tambah\n2) hapus\n3) reset\n4)selesai\n\npilihan\t:"))
   
    if y=="1":
        read()
        inputData()
        save(item.x,item.x_price)
        
    elif y=="2":
        read()
        delete(input("input number to delete"))
        
    elif y=="3":
        item.x=[]
        item.x_price=[]
        
    else:
        end=input("apakah sudah selesai(y/n):\n")
    
