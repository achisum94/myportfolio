class car:
    def __init__(self, p_make, p_model, p_miles):
        self.__make=p_make
        self.__model=p_model
        self.__miles=p_miles
        
    def get_make(self):
        return self.__make
    
    def get_model(self):
        return self.__model
    
    def get_miles(self):
        return self.__miles
    

class car__with__price(car):
    def __init__(self, p_make, p_model, p_miles, p_price):
        car.__init__(self, p_make, p_model, p_miles)
        self.__price= price

    def get_price(self):
        return self.__price
        
def main():
    print()
    make=input('enter car make: ')
    model=input('enter car model: ')
    miles=input('enter the miles: ')
    
    my_car=car(make, model, miles)
    print ('here is the data you entered: ')
    show_data(my_car)
    print()
    print('do you want to add the price also before uploading? ')
    add_price=input('enter y for yes and n for no\n ')
    
    if add_price.lower()=='y':
        price=int(input('what is the price'))
        print()
        my_car=car_with_price(make, model, miles. str(format(price, ',d')))
        print('the price $',my_car.get_price(),' has been assigned to the car', sep='')
        
def show_data(my_car):
    print('make:', my_car.getmake())
    print('model:', my_car.getmodel())
    print('miles:', my_car.getmiles())
    
    
    
        
    