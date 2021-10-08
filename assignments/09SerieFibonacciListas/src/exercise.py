def main():
    x=-1
    su= 0
    a=1
    b=1
    lista=[]
    while x <=-1:
        x=int(input())
    if x==0:
        print(lista)  

    elif x==2:
        lista.append(0)
        lista.append(1)
        print(lista)
    else: 
        lista.append(0)
        lista.append(1)
        lista.append(1)
        for i in range(x-3):
            su=a+b
            b=a
            a=su
            lista.append(su)
        print(lista)    
                  

if __name__=='__main__':
    main()
