from Reto10_1 import adicionlista
if __name__ == "__main__":
    l1=[]
    l2=[]
    adicionlista(l1,True)
    adicionlista(l2,False)
    i=0
    c=0
    if len(l1)!=len(l2):
        print("Las listas deben ser del mismo tamaño")
        exit()
    while i <= ((len(l1))-1):
        
        c=c+l1[i]*l2[i]
        i+=1
    print("El producto punto de las listas es: ",c)