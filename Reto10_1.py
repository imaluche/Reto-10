def adicionlista(l:list,k:bool):
    i=1
    while i==1:
        e= float(input("ingresa un numero, si no ingresas un numero entero o decimal el programa no funcionara correctamente:"))
        l.append(e)
        i=int(input("deseas ingresar otro numero? (1, cualquier otro numero para no)"))
    if k==True: print("nuestra primera lista fue: "+ str(l)+ ", la siguiente lista no debe tener mas de "+ str(len(l))+" elementos")
    else: print("nuestra segunda lista fue: "+ str(l)+ ", tiene "+ str(len(l))+" elementos.")
p:list=[]
if __name__ == "__main__":
    adicionlista(p,False)
    print(p)
    D=sum(p)
    print(D)
    d=len(p)
    ac:float= D/d
    print("el promedio de la lista "+ str(p)+" es "+ str(ac))