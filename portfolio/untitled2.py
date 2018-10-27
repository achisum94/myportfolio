
    #the intializer function
def __init__(self, model, year):
        
        #we going to create 3 dictionaries, one for each model
        #the year of make will be the key, and the price will be the value
        prius={2014:10000, 2015:12000, 2016:14000, 2017:20000, 2018:28000}

        camry={2014:13000, 2015:16000, 2016:20000, 2017:23000, 2018:28000} 

        highlander={2014:15000, 2015:19000, 2016:22000, 2017:26000, 2018:32000}

        if model==1:
            self.__price=prius[year]
        elif model==2:
            self.__price=camry[year]
        else:
            self.__price=highlander[year]
            
    #this function will called whenever object passed as
    #to print command or to str function
def __str__(self):
        return str(format(self.__price, ',d'))
        
    
def main():
    #ask from the user
    #to enter model and year
        
    print('please enter the number that correspondes to your model choice')
    print('1. Prius\n'\
         '2. Camry\n','3. Highlander',sep='')
    print()
    model=int(input())
    print()
    year=int(input('enter the year of make starting from 2014\n '))
        
    my_car=(model, year)
        
    #show to customer estimated price
    print('estimated price: $    ',my_car,sep='')
    
main()