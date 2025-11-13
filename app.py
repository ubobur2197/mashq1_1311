# 1
class BankAccount:
    def __init__(self, account_number, customer_name, balance=0):
        self.__account_number = account_number
        self.__customer_name = customer_name
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} so'm qo'shildi. Joriy balans: {self.__balance}")
        else:
            print("Summani to'g'ri kiriting!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} so'm yechildi. Joriy balans: {self.__balance}")
        else:
            print("Yetarli mablag‘ mavjud emas!")

    def get_balance(self):
        return self.__balance



class PremiumAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance=0, discount_rate=0.05):
        super().__init__(account_number, customer_name, balance)
        self.discount_rate = discount_rate

    def apply_discount(self, service_fee):
        return service_fee * (1 - self.discount_rate)



# 2
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary

    def get_salary(self, requester):
        if isinstance(requester, Manager):
            return self.__salary
        else:
            return "maxfiy"

    def set_salary(self, requester, new_salary):
        if isinstance(requester, HR):
            self.__salary = new_salary
            print(f"{self.name} ish haqi yangilandi: {new_salary}")
        else:
            print("Sizda bu amalni bajarish huquqi yo‘q!")


class Manager(Employee):
    pass


class HR(Employee):
    pass



# 3
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.__price = price
        self.__stock = stock

    def purchase(self, quantity):
        if self.__stock >= quantity:
            self.__stock -= quantity
            print(f"{quantity} dona {self.name} sotib olindi.")
        else:
            print(f"{self.name} — sotuvda yo‘q yoki yetarli emas!")

    def get_stock(self):
        return self.__stock


class InventoryManager:
    def update_stock(self, product, new_stock):
        product._Product__stock = new_stock
        print(f"{product.name} zaxirasi yangilandi: {new_stock}")



# 4
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.__grades = []

    def add_grade(self, grade):
        self.__grades.append(grade)
        print(f"{self.name} uchun {grade} baho qo‘shildi.")

    def get_average(self):
        if self.__grades:
            return sum(self.__grades) / len(self.__grades)
        return 0.0


class Teacher:
    def add_student_grade(self, student, grade):
        student.add_grade(grade)



# 5
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def accelerate(self, amount):
        self.__speed += amount
        print(f"Tezlik oshdi: {self.__speed} km/h")
        if self.__speed > 200:
            print("⚠️ Xavfli tezlik!")

    def brake(self, amount):
        self.__speed = max(0, self.__speed - amount)
        print(f"Tormoz bosildi: {self.__speed} km/h")

    def get_speed(self):
        return self.__speed


class CarControlSystem:
    def monitor(self, car):
        speed = car._Car__speed
        if speed > 200:
            print(f"{car.brand} {car.model}: ⚠️ Tezlik juda yuqori!")
        else:
            print(f"{car.brand} {car.model}: tezlik normal ({speed} km/h).")
