from Reto10_1 import adicionlista
if __name__ == "__main__":
    p:list=[]
    adicionlista(p,False)
    for i in p:
        if i/10==i//10:
            p.pop(p.index(i))
            p.append(i)
    print(p)