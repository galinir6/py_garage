import json
import os
from enum import Enum

from helper import load_list, save_list

# enum
class Actions(Enum):
    PRINT = 1
    ADD = 2
    SEARCH = 3
    DELETE = 4
    EXIT = 5

cars = []
data_file = 'cars.json'

# print enum actions
def menu():
    for x in Actions: print(f'{x.value} - {x.name}')
    return Actions(int(input("Enter your selection:")))

# actions functions
def main():
    global cars
    os.system('cls' if os.name == 'nt' else 'clear')
    cars = load_list(data_file , cars)
    while(True):
     userSelection = menu()
     if userSelection == Actions.PRINT: print(cars) 
     if userSelection == Actions.ADD: add_car()
     if userSelection == Actions.SEARCH: print(search())
     if userSelection == Actions.DELETE: del_car()
     if userSelection == Actions.EXIT: exit_func()

# add a car
def add_car():
   cars.append({"brand" : input("Car brand:") , "model" : input("Car model:") ,"color" : input("Car color:")})
   print('Car has been added!')

# exit program
def exit_func():
    print("Bye")
    save_list(data_file , cars)
    exit()

# search a car
def search():
    global cars
    find_car = input('Enter car brand: ')
    for car in cars:
       if car["brand"] == find_car:
          return car
    print('car was not found...')

# remove a car
def del_car():
   global cars
   del_car = input('Enter car to remove: ')
   for car in cars:
      if car["brand"] == del_car:
         cars.remove(car)
         print(f'{del_car} has been removed!')
         return

if __name__ == "__main__":
    main()