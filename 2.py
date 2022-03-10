from functools import partial
import tkinter as tk

root= tk.Tk()

canvas= tk.Canvas(root, height=700, width=700, bg="white")
canvas.pack()
frame =tk.Frame(root, bg="blue")
frame.place(relwidth= 0.8,relheight=0.2, relx=0.1, rely=0.1)
frame2=tk.Frame(root, bg="green", padx=4,pady=8)
frame2.place( relx=0.7, rely=0.1)
frame3 =tk.Frame(root, bg="cyan")
frame3.place(relwidth= 0.8,relheight=0.2, relx=0.1, rely=0.3)


class item:
    x=["ayam","sapi","ikan"]
    x_price=[2, 6, 8]
    
finalLi= []
finalPrice=[]
def addtolist(a):
    finalLi.append(item.x[a])
    finalPrice.append(item.x_price[a])
    print(item.x[a], item.x_price[a])
    tk.Label(frame3, text=(item.x[a],item.x_price[a])).pack()
    
def showTotal():
    eztotal = {item:finalLi.count(item) for item in finalLi}
    tk.Label(frame2, text=("total=",eztotal)).pack()
    tk.Label(frame2, text=(sum(finalPrice))).pack()
for i in range(0,len(item.x)):
    tk.Button(frame, text=(item.x[i],item.x_price[i]), command=partial(addtolist, i),).pack()
   
        
tk.Button(frame2, text=("show total"), command= showTotal).pack()    

        

    
      
    
root.mainloop()
print(finalLi)
print(sum(finalPrice))