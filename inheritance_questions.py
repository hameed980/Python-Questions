print("hello world")
# Python Inheritance Practice Questions

# 1. Single Inheritance
# Single inheritance is when a child class inherits from only one parent class.
# Questions:
# 1.)Write a Python program where a Person class has a method to display name and age, and a Student class inherits it.
# 2.)Create a parent class Animal with a method make_sound. The child class Dog should inherit from Animal and override the make_sound method to bark.
# 3.)Implement a class Vehicle with a method details. Create a subclass Car that inherits Vehicle and adds its own attribute model.
# 4.)Write a program to demonstrate how private members of the parent class are inaccessible to the child class.
# 5.)Create a parent class BankAccount with methods to deposit and withdraw. The child class SavingsAccount should inherit and add an interest rate method.

# 2. Multilevel Inheritance
# Multilevel inheritance occurs when a child class inherits from another child class.
# Questions:
#1.) Create a Grandparent, Parent, and Child class to demonstrate multilevel inheritance. Add unique methods in each class.
#2.) Implement a Device class with a turn_on method. The Mobile class inherits Device, and the Smartphone class inherits Mobile.
#3.) Write a program to calculate the area of shapes using classes Shape, Rectangle, and Square in a multilevel inheritance setup.
#4.) Implement a chain of classes: LivingBeing -> Animal -> Bird with methods showcasing the inheritance.
#5.) Write a program demonstrating how constructors are called in multilevel inheritance.

# 3. Hierarchical Inheritance
# Hierarchical inheritance occurs when multiple child classes inherit from the same parent class.
# Questions:
# 1.)Create a base class Animal with a method move. Create two child classes Fish and Bird inheriting from Animal, with their own specific methods.
# 2.)Implement a parent class Shape with a draw method. Create two child classes Circle and Triangle, overriding the draw method.
# 3.)Write a program to demonstrate the concept of hierarchical inheritance using a parent class Device and child classes Phone and Laptop.
# 4.)Create a class Account with a method to show balance. Derive two classes SavingsAccount and CurrentAccount from it, adding unique features.
# 5.)Write a program where a Person class is inherited by Employee and Student, each adding unique attributes and methods.

# 4. Multiple Inheritance
# Multiple inheritance occurs when a class inherits from more than one parent class.
# Questions:
#1.) Create two parent classes Mother and Father. The child class Child inherits from both and uses attributes/methods from both parents.
#2.) Implement two classes Car and Boat. Create a child class AmphibiousVehicle that inherits from both and demonstrates features of both.
#3.) Write a program where two classes Flyable and Swimmable are inherited by a class Duck, showing combined functionality.
#4.) Create classes Reader and Writer. Derive a child class Editor that combines their functionalities.
#5.) Write a program to demonstrate how the super() function resolves the method resolution order (MRO) in multiple inheritance.