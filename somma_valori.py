def somma_elementi_lista(mia_lista):
    somma = sum(mia_lista)
    return somma
    
def somma_elementi_lista_2(mia_lista):
    sum=0
    for element in mia_lista:
        sum=sum+element
        # oppure sum += element
    return sum
