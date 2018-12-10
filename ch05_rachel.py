# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 10:08:33 2018

@author: 612383461
"""


class Animal(object):
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
       
    def eat(self):
        print('yum')

class Pet(Animal):
    def __init__(self, name='Pet', age=0):
        Animal.__init__(self, name, age=0)
        self.name = name
        self.age = age
        
    def greet(self):
        print('runs to human')

    def choose_animal(self):
        pet = input("Do you prefer cats or dogs? ")
        name = input("What would you like to call your pet? ")
        age = input("How old is {}? ".format(name))
        if pet == "cats":
            cat = Cat(name, age, 0)
            cat.jump_on_human()
        elif pet == "dogs":
            dog = Dog(name, age, 0)
            dog.choose_trick()
        else:
            print("that is not an animal")


class Dog(Pet):
    
    def __init__(self, name, age, treats=0):
        Pet.__init__(self, name, age=0) 
        self.name = name
        self.age = age
        self.treats = treats

    def bark(self):
        print('Woof!')

    def choose_trick(self):
        print('How many treats do you want to give {}?'.format(self.name))
        treatAmount = int(input())
        self.treats += treatAmount
        while 0 < self.treats < 10:
            print(self.treats)
            Dog.do_trick(self)
            print('How many treats do you want to give {}?'.format(self.name))
            treatAmount = int(input())
            self.treats += treatAmount
        print('tired now')
        
             
    def do_trick(self):
        response = input("Would you like {} to do a trick? y/n ".format(self.name))[0]
        if response == "y":
            if self.treats < 0:
                print('Cannot have a negative number of treats!')
            elif self.treats <= 2:
                print('brings a toy')
            elif self.treats <= 4:
                print('rolls over')
            elif self.treats <= 6:
                print('spins in a circle')
            elif self.treats <= 8:
                print('lies down')
            else:
                self.treats <= 10
                print('sits')

        elif response == "n":
            print("Ok, {} curls up and goes to sleep.".format(self.name))
            self.treats = 11
        else:
           print("you must choose yes or no")
           self.treats = 11     
 
class Cat(Pet):
    def __init__(self, name, age=0, NumberofStrokes=0):
        Animal.__init__(self, name, age=0)
        self.NumberofStrokes = NumberofStrokes
        
    def meow(Cat):
        print('Meow')
        
    def jump_on_human(self):
        print('How many times do you want to stroke {}?'.format(self.name))
        self.NumberofStrokes = int(input())
      
        if self.NumberofStrokes < 0:
            raise RuntimeError('Cannot stroke a cat a negative number of times!') 
        elif self.NumberofStrokes < 20:
            print('Purr '*self.NumberofStrokes)
        else:
            print('Purr'+('r'*self.NumberofStrokes))
            
Pet.choose_animal(Pet)


