СURRENCY = {'UAH': 1, 'USD': 28, 'EUR': 32}


class Product:
    def __init__(self, name, real_price, price, weight):
        self.name = name
        self.real_price = real_price
        self.price = price
        self.weight = weight

    def register(self):
        self.name = input("Введіть назву товару:")
        while True:
            try:
                self.real_price = float(
                    input("Введіть собівартість товару в гривнях:"))
                if self.real_price > 0:
                    break
            except ValueError:
                print("Ви можете вводити лише додатні числа")

        while True:
            try:
                self.price = float(input("Введіть ціну товару в гривнях:"))
                if self.price > 0:
                    break
            except ValueError:
                print("Ви можете вводити лише додатні числа")
        while True:
            try:
                self.weight = float(input("Введіть вагу товару:"))
                if self.weight > 0:
                    break
            except ValueError:
                print("Ви можете вводити лише додатні числа")
        return 'Реєстрація товару пройшла успішно'

    def get_recalculation_of_price(self, customer):
        coefficient = СURRENCY[customer.currency]
        return self.price / coefficient

    def __str__(self):
        return '\nНазва: {}\nЦіна(у гривнях): {}\nВага: {}\n'.format(
            self.name, self.price, self.weight)


class Customer:
    def __init__(self, name, discount, currency):
        self.name = name
        self.discount = discount
        self.currency = currency

    def register(self):
        self.name = input("Введіть ім'я покупця:")
        while True:
            try:
                self.discount = float(input("Введіть відсоток знижки користувача:"))
                if self.discount > 100 or self.discount < 0:
                    print("Знижка не може бути більшою ніж 100% і меньшою ніж 0%")
                else:
                    break
            except ValueError:
                print("Ви можете вводити лише числа")
        while True:
            self.currency = input("Введіть валюту користувача ('UAH', 'USD', 'EUR'): ")
            if self.currency in СURRENCY:
                break

    def __str__(self):
        return '\nІм\'я: {}\nВідсоток знижки: {}\nВалюта: {}\n'.format(
            self.name, self.discount, self.currency)


class Buy(Product):
    def __init__(self, product, customer, num):
        self.product = product
        self.customer = customer
        self.num = num

    @property
    def all_price(self):
        no_discount = self.num * self.product.get_recalculation_of_price(self.customer)
        return round((100-self.customer.discount)/100 * no_discount, 2)

    @property
    def all_weight(self):
        return self.num * self.product.weight

    def __str__(self):
        buy_str = '\nКількість купленого товару: {}\nПідсумкова ціна: {} {}\nПідсумкова вага: {}\n'
        return buy_str.format(self.num, self.all_price, self.customer.currency, self.all_weight)


class Check(Buy):
    def __init__(self, buy):
        self.buy = buy

    def __str__(self):
        check = '\nІнформація про продукт:\n{}\nІнформація про покупця:\n{}\nІнформація про покупку:\n{}\n'
        check = check.format(str(self.buy.product), str(self.buy.customer), str(self.buy))
        return check


def register_product():
    new_product = Product(0, 0, 0, 0)
    new_product.register()
    return new_product


def register_customer():
    new_customer = Customer(0, 0, 0)
    new_customer.register()
    return new_customer


def buy_product(customer, product):
    while True:
        try:
            num = int(input("Введіть кількість товару котру Ви хотілиб купити: "))
            if num >= 0:
                break
        except ValueError:
            print('Вводити можна лише додатні цілі числа')
    items = Buy(product, customer, num)
    return items


def show_check(items):
    check = Check(items)
    return check


products = []
customers = []
num_iter_prod = 0
num_iter_cust = 0
buy_prod = 0

while True:
    print("Натисніть 1 щоб зареєструвати нового покупця")
    print("Натисніть 2 щоб зареєструвати новий товар")
    print("Натисніть 3 щоб купити продукт")
    print("Натисніть 4 щоб отримати чек")
    print("Натисніть 5 щоб вийти")

    case = input("-->")
    if case == '1':
        new_customer = register_customer()
        print("Новий покупець")
        print(new_customer)
        customers.append(new_customer)
        num_iter_prod += 1
    elif case == '2':
        new_product = register_product()
        print("Новий товар")
        print(new_product)
        products.append(new_product)
        num_iter_cust += 1
    elif case == '3':
        if products != [] and customers != []:
            print("_____Товари_____")
            for i in range(len(products)):
                print("#", i, end='')
                print(products[i])
            print("_____Покупці_____")
            for j in range(len(customers)):
                print("#", j, end='')
                print(customers[j])
            while True:
                try:
                    num_prod = int(input("Введіть номер товара котрий купуєте: "))
                    if 0 <= num_prod < num_iter_prod:
                        break
                except ValueError:
                    print('Вводити можна лише цілі числа')
            while True:
                try:
                    num_cust = int(
                        input("Введіть номер користувача котрим купувати товар: "))
                    if 0 <= num_cust < num_iter_cust:
                        break
                except ValueError:
                    print('Вводити можна лише цілі числа')
            buy_prod = buy_product(customers[num_cust], products[num_prod])
            print("_"*10)
            print(buy_prod)
            print("_"*10)
        else:
            print("Добавте покупця або товар")
    elif case == '4':
        if buy_prod:
            print("_"*10)
            print(show_check(buy_prod))
            print("_"*10)
        else:
            print("Оберіть і купіть товар")
    elif case == '5':
        break
