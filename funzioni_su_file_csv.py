def sum_csv(file_name):


    values=[]

    my_file=open(file_name,'r')
    for line in my_file:

        elements=line.split(',') #variabile chiara e definita

        #devo saltare l'intestazione
        if elements [0] != 'Date': #se il primo elemento è diverso da Date.
            date= elements[0]
            #print(date)
            value=float(elements[1])
            #print(value)
            values.append(value)

    somma_complessiva =sum(values)

    my_file.close()
    return somma_complessiva