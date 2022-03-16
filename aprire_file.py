#Apro il file
my_file = open('shampoo_sales.csv','r') #read
# ci sono altri modi che permettono di evitare la close
#KLeggo il il contenuto
my_file_contents = my_file.read()

if len (my_file_contents)>10:
    print(my_file_contents[0:10]+'...')
else:
    print(my_file_contents)
    
#print(my_file.read())
#print(my_file.read()[0:20])

my_file.close() # mi permette di ottimizzare la risorsa


my_file = open('shampoo_sales.csv','r') # contatore ad oggetto sul disco
# non carica tutto il file in memoria, ma solo un pezzetto
for line in my_file:
    print(line)

my_file.close()

my_file=open('saluti.txt','w')
my_file.write('Ciao mondo!')
my_file.close()