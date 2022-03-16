#Inizializzo
values=[]

#Apro e eleggo il file, linea per linea
my_file=open('shampoo_sales.csv','r')
for line in my_file:

    elements=line.split(',') #variabile chiara e definita


    #devo saltare l'intestazione
    if elements [0] != 'Date': #se il primo elemento è diverso da Date. NB non è un         #check forte
        date= elements[0]
        value=elements[1]

    values.append(value)

print(values)