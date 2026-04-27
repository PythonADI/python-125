# Workshop 7 - Practical Examples

# ==============================
# Example 1: Bank with multiple accounts
# ==============================

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self.balance})"


class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def open_account(self, owner, balance=0):
        account = Account(owner, balance)
        self.accounts.append(account)
        return account

    def total_assets(self):
        return sum(a.balance for a in self.accounts)

    def find(self, owner):
        for a in self.accounts:
            if a.owner == owner:
                return a
        return None


bank = Bank("First National")
bank.open_account("Alice", 500)
bank.open_account("Bob", 1200)
bank.open_account("Carol", 80)

bank.find("Bob").withdraw(200)
bank.find("Alice").deposit(100)

print(bank.accounts)
print(f"Total assets: ${bank.total_assets()}")


# ==============================
# Example 2: Shopping cart
# ==============================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} (${self.price:.2f})"


class Cart:
    def __init__(self):
        self.items = []     # list of (Product, quantity)

    def add(self, product, quantity=1):
        self.items.append((product, quantity))

    def total(self):
        return sum(p.price * q for p, q in self.items)

    def show(self):
        print("Cart:")
        for product, q in self.items:
            line_total = product.price * q
            print(f"  {product} x {q} = ${line_total:.2f}")
        print(f"Total: ${self.total():.2f}")


apple = Product("Apple", 0.50)
bread = Product("Bread", 2.00)
milk = Product("Milk", 3.50)

cart = Cart()
cart.add(apple, 6)
cart.add(bread, 2)
cart.add(milk, 1)
cart.show()


# ==============================
# Example 3: Library with inheritance
# ==============================

class Item:
    def __init__(self, title):
        self.title = title
        self.borrowed = False

    def borrow(self):
        if self.borrowed:
            print(f"{self.title} is already borrowed.")
            return False
        self.borrowed = True
        return True

    def return_item(self):
        self.borrowed = False

    def __repr__(self):
        status = "out" if self.borrowed else "available"
        return f"{self.title} [{status}]"


class Book(Item):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def __repr__(self):
        return f"Book: {self.title} by {self.author} - {'out' if self.borrowed else 'available'}"


class Movie(Item):
    def __init__(self, title, director):
        super().__init__(title)
        self.director = director

    def __repr__(self):
        return f"Movie: {self.title} dir. {self.director} - {'out' if self.borrowed else 'available'}"


class Library:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def available(self):
        return [i for i in self.items if not i.borrowed]


lib = Library()
lib.add(Book("Clean Code", "Robert Martin"))
lib.add(Book("The Pragmatic Programmer", "Hunt & Thomas"))
lib.add(Movie("Inception", "Christopher Nolan"))

lib.items[0].borrow()
lib.items[2].borrow()

for item in lib.items:
    print(item)

print(f"Available: {len(lib.available())}")


# ==============================
# Example 4: Game characters
# ==============================

class Character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        self.max_hp = hp

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        self.hp = max(0, self.hp - amount)
        print(f"{self.name} takes {amount} damage. HP: {self.hp}/{self.max_hp}")
        if not self.is_alive():
            print(f"{self.name} has fallen!")

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"{self.name} heals {amount}. HP: {self.hp}/{self.max_hp}")


class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, hp=120)
        self.attack_power = 25

    def attack(self, target):
        print(f"{self.name} swings a sword at {target.name}!")
        target.take_damage(self.attack_power)


class Mage(Character):
    def __init__(self, name):
        super().__init__(name, hp=80)
        self.attack_power = 35

    def attack(self, target):
        print(f"{self.name} casts a fireball at {target.name}!")
        target.take_damage(self.attack_power)


hero = Warrior("Aragorn")
enemy = Mage("Saruman")

hero.attack(enemy)
enemy.attack(hero)
hero.heal(10)
hero.attack(enemy)
hero.attack(enemy)
