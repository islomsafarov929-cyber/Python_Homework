# Task 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self) -> float:
        return (self.radius ** 2) * math.pi
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius  


# Task 2.Write a Python program to create a Person class. Include attributes like name, country, and date of birth. Implement a method to determine the person's age.

from datetime import datetime

class Person:
    def __init__(self, name: str, country: str, birth_date: datetime):
        self.name = name
        self.country = country
        self.birth_date = birth_date

    def age(self) -> int:
        today = datetime.now().date()
        years = today.year - self.birth_date.year


        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1

        return years


# Example usage
p = Person("Alice", "USA", datetime(2000, 12, 25))
print(f"{p.name} from {p.country} is {p.age()} years old.")


# Task 3.Write a Python program to create a Calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, num1 : float, num2 : float,):
        self.num1 = num1
        self.num2 = num2

    def addition(self) -> float:
        return self.num1 + self.num2
    
    def difference(self) -> float:
        return abs(self.num1 - self.num2)
    
    def product(self) -> float:
        return self.num1 * self.num2
    
    def division(self) -> float:
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            raise ZeroDivisionError("Division by zero is not allowed")
        

# Task 4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter. Implement subclasses for different shapes like Circle, Triangle, and Square.

import math

# Base class
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement perimeter()")


# Circle subclass
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Triangle subclass
class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


# Square subclass
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# Example usage
circle = Circle(5)
triangle = Triangle(3, 4, 5)
square = Square(6)

print("Circle: Area =", circle.area(), ", Perimeter =", circle.perimeter())
print("Triangle: Area =", triangle.area(), ", Perimeter =", triangle.perimeter())
print("Square: Area =", square.area(), ", Perimeter =", square.perimeter())


# Task 5. Write a Python program to create a class representing a binary search tree. Include methods for inserting and searching for elements in the binary tree.


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key: int):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current: Node, key: int):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)
        # If key == current.key, do nothing (no duplicates)

    def search(self, key: int) -> bool:
        return self._search(self.root, key)

    def _search(self, current: Node, key: int) -> bool:
        if current is None:
            return False
        if key == current.key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    def inorder(self):
        """Return inorder traversal as a list"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current: Node, result: list):
        if current:
            self._inorder(current.left, result)
            result.append(current.key)
            self._inorder(current.right, result)


# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Inorder Traversal:", bst.inorder())
print("Search 40:", bst.search(40))   # True
print("Search 25:", bst.search(25))   # False


# Task 6. Write a Python program to create a class representing a stack data structure. Include methods for pushing and popping elements.

class Stack:
    def __init__(self):
        self.items = []   # internal list to store stack elements

    def push(self, item):
        """Add an element to the top of the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the top element of the stack"""
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Pop from empty stack")

    def peek(self):
        """Return the top element without removing it"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack"""
        return len(self.items)


# Example usage
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print("Stack size:", stack.size())       # 3
print("Top element:", stack.peek())      # 30
print("Popped element:", stack.pop())    # 30
print("Stack size after pop:", stack.size())  # 2


# Task 7.Write a Python program to create a class representing a linked list data structure. Include methods for displaying linked list data, inserting, and deleting nodes.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        """Display all nodes in the linked list"""
        current = self.head
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Linked List:", elements)

    def insert(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, key):
        """Delete the first node with the given data"""
        current = self.head

        # If head node itself holds the key
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Search for the key
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If key not found
        if current is None:
            print(f"Value {key} not found in the list.")
            return

        # Unlink the node
        prev.next = current.next
        current = None


# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()          # Linked List: [10, 20, 30]

ll.delete(20)
ll.display()          # Linked List: [10, 30]

ll.delete(40)         # Value 40 not found in the list.

# Task 8.Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

class ShoppingCart:
    def __init__(self):
        self.items = []
        
    def add_item(self, name : str, price : float, quantity : int):

        itemm = {'name' : name, 'price' : price, 'quantity' : quantity}
        self.items.append(itemm)

    def remove_item(self, item_name: str):
        for item in self.items:
            if item['name'] == item_name:
                self.items.remove(item)
                print(f"{item_name} removed from cart.")
                return
        print("Item not found.")

    def calculate_total(self) -> float:
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total
    
cart = ShoppingCart()
cart.add_item("Olma", 5000, 2)
cart.add_item("Banan", 8000, 1)

cart.remove_item('Banan')
        

# Task 9.Write a Python program to create a class representing a stack data structure. Include methods for pushing, popping, and displaying elements.

class Stack:
    def __init__(self):
        # Stackni list orqali saqlaymiz
        self.items = []

    def push(self, item):
        """Elementni stackga qo'shish"""
        self.items.append(item)
        print(f"{item} pushed onto stack.")

    def pop(self):
        """Stackdan elementni olib tashlash va qaytarish"""
        if not self.is_empty():
            removed = self.items.pop()
            print(f"{removed} popped from stack.")
            return removed
        else:
            print("Stack is empty. Nothing to pop.")
            return None

    def display(self):
        """Stackdagi elementlarni ko'rsatish"""
        if not self.is_empty():
            print("Stack elements (top → bottom):")
            for item in reversed(self.items):
                print(item)
        else:
            print("Stack is empty.")

    def is_empty(self):
        """Stack bo'sh yoki yo'qligini tekshirish"""
        return len(self.items) == 0
    

stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

stack.display()

stack.pop()
stack.display()

stack.is_empty()

# Task 10.Write a Python program to create a class representing a queue data structure. Include methods for enqueueing and dequeueing elements.

class Queue:
    def __init__(self):
        # Queue elementlarini listda saqlaymiz
        self.items = []

    def enqueue(self, item):
        """Elementni queue oxiriga qo'shish"""
        self.items.append(item)
        print(f"{item} enqueued.")

    def dequeue(self):
        """Queue boshidan elementni olib tashlash va qaytarish"""
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"{removed} dequeued.")
            return removed
        else:
            print("Queue is empty. Nothing to dequeue.")
            return None

    def is_empty(self):
        """Queue bo'sh yoki yo'qligini tekshirish"""
        return len(self.items) == 0

    def display(self):
        """Queue elementlarini ko'rsatish"""
        if not self.is_empty():
            print("Queue elements (front → rear):")
            for item in self.items:
                print(item)
        else:
            print("Queue is empty.")


# Task 11.Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

class Bank:
    def __init__(self, name: str):
        # Bank nomi va mijozlar ro'yxati
        self.name = name
        self.customers = {}

    def create_account(self, customer_name: str, initial_balance: float = 0.0):
        """Yangi mijoz uchun hisob ochish"""
        if customer_name in self.customers:
            print(f"Account already exists for {customer_name}.")
        else:
            self.customers[customer_name] = initial_balance
            print(f"Account created for {customer_name} with balance {initial_balance}.")

    def deposit(self, customer_name: str, amount: float):
        """Hisobga pul qo'shish"""
        if customer_name in self.customers:
            self.customers[customer_name] += amount
            print(f"{amount} deposited to {customer_name}'s account.")
        else:
            print("Customer not found.")

    def withdraw(self, customer_name: str, amount: float):
        """Hisobdan pul yechish"""
        if customer_name in self.customers:
            if self.customers[customer_name] >= amount:
                self.customers[customer_name] -= amount
                print(f"{amount} withdrawn from {customer_name}'s account.")
            else:
                print("Insufficient funds.")
        else:
            print("Customer not found.")

    def check_balance(self, customer_name: str):
        """Hisobdagi balansni ko'rish"""
        if customer_name in self.customers:
            print(f"{customer_name}'s balance: {self.customers[customer_name]}")
            return self.customers[customer_name]
        else:
            print("Customer not found.")
            return None

    def display_customers(self):
        """Barcha mijozlar va balanslarini ko'rsatish"""
        if self.customers:
            print(f"Customers of {self.name}:")
            for name, balance in self.customers.items():
                print(f"{name}: {balance}")
        else:
            print("No customers in the bank.")
