class CSVFile():
    
    def __init__(self,name):
        self.name = name
        
    def get_data(self):
        list=[]
        my_file=open(self.name,'r')
        for line in my_file:
            elements=line.split(',')
            elements[-1]=elements[-1].strip()
            if elements[0] != 'Date':
                #date=element[0]
                #value=element[1]
                list.append(elements)
        my_file.close()
        return list

                
        
file=CSVFile('shampoo_sales.csv')            
print(file.get_data())