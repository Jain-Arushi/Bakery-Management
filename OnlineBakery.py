'''
facilities: messages, view menu 
1. admin login : add new item | delete item | change item price
2. customer : billing | customer name, phone number
3. exit


'''

import sqlite3
import time

connection = sqlite3.connect('menu.db')
cursor = connection.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS Menu([product_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
                [product_name] TEXT, 
                [product_price] INTEGER)''')

query = '''SELECT *  FROM Menu'''
cursor.execute(query)
results = cursor.fetchall()
if results==[]:
    cursor.execute('''
                    INSERT INTO Menu (product_name, product_price)
                    VALUES
                    ('Cake',400),
                    ('Bread',50),
                    ('Cookies',100),
                    ('Doughnuts',80),
                    ('Pie',120)
                    ''')
    connection.commit()


def display_items(cursor):
    query='''SELECT * FROM Menu'''
    cursor.execute(query)
    results=cursor.fetchall()
    print("List of items: ")
    print("ID","Name","Price",sep=" ")
    for each in results:
        print(each[0],each[1],each[2],sep=" ")


def admin_login(connection,cursor):
    print()
    print("---------Welcome! You are logged in as Admin!----------")
    print()
    print("Here are the list of choices:")
    print("Choice 1: Add an item",
            "Choice 2: Remove an item",
            "Choice 3: Update item price",
            "Choice 4: See all the items",
            "Choice 5:Exit",
            sep="\n")

    choice = int(input("Enter your choice: "))
    print()
    time.sleep(0.5)

    if choice==1:
        print("What you like to add?")
        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")

        try:
            query=f'''INSERT INTO Menu(product_name, product_price) VALUES ('{product_name}','{product_price}')'''
            cursor.execute(query)
            connection.commit()
            print("The item has been added to the list!")
        except Exception as e:
            print("Error occured!")

        time.sleep(1)
        admin_login(connection,cursor)

    elif choice==2:
        display_items(cursor)
        print("Which item you would like to remove?")
        id = int(input("Enter product id:"))
        try:
            query=f'''DELETE FROM Menu WHERE product_id={id}'''
            cursor.execute(query)
            connection.commit()
            print("The item has been removed from the shop!")
        except Exception as e:
            print("Invalid item!")
        time.sleep(1)
        admin_login(connection,cursor)

    elif choice==3:
        display_items(cursor)
        print("Which item price you would like to update?")
        id=int(input("Enter product ID:"))
        price=int(input("Enter the updated price:"))
        try:
            query=f'''UPDATE Menu SET product_price={price} WHERE product_id={id}'''
            cursor.execute(query)
            connection.commit()
            print("The item price has been updated!")
        except Exception as e:
            print("Invalid Product ID!")

        time.sleep(1)
        admin_login(connection,cursor)

    elif choice==4:
        display_items(cursor)
        time.sleep(1.5)
        admin_login(connection,cursor)
    elif choice==5:
        main()
    else:
        print("Invalid Choice!")
        time.sleep(1)
        admin_login(connection,cursor)

def customer_login(connection,cursor):
    print("-----------Welcome,You are logged in as a biller!-------------")
    print("Here is the list of choices:")
    print("Choice 1: Billing", "Choice 2: Exit",sep="\n")
    choice = int(input("Enter your choice:"))
    if(choice==1):
        name = input("Enter the customer name:")
        print(f"What do you wanna buy {name}?")
        time.sleep(0.5)
        display_items(cursor)

        print()
        total = 0
        items=[]
        while 1:

            id=int(input("Enter the product ID:"))
            quantity =int(input("Enter the quantity:"))
            try:
                query=f'''SELECT * FROM Menu WHERE product_id={id}'''
                cursor.execute(query)
                result=cursor.fetchone()

                total += result[2]*quantity
                items.append([result[1],quantity])
                i=input("Anything else?Answer Y for Yes and N for No! ")
                if(i=='N'):
                    break
            except Exception as e:
                print("Invalid Entry!")
                print(e)
                break

        if(total!=0):
            print()
            print("---------Sweet Dough Bakery--------")
            print("-------Billing Details-------")
            print(f"Name:{name}")
            print(f"Items:")
            for each in items:
                print(each[0],each[1],sep=":")
            print(f"Total: {total}")
            print("Thank you! Have a sweet day!")
            print()

        time.sleep(1)
        customer_login(connection,cursor)
    elif choice==2:
        main()
    else:
        print("Invalid Choice!")
        time.sleep(1)
        customer_login(connection,cursor)

def main():
    inloop = 1
    while inloop:
        print()
        print("---------------------------------------------------------------------")
        print("---------------------Welcome to Swweet Dough Bakery!---------------------")
        print("---------------------------------------------------------------------")

        print("How you want to Enter?")
        print("Choice 1: Admin Login","Choice 2: Customer Login", "Choice 3: Exit",sep="\n")


        choice = input("Enter your choice:")

        if choice=='1':
            password = input("Enter the password: ")
            if password=="Arushi":
                admin_login(connection,cursor)
            else:
                print("Incorrect Password!")
                time.sleep(1)

        elif choice=='2':
            customer_login(connection,cursor)
        elif choice=='3':
            exit()
        else:
            print("Invalid Choice!")

main()'''
facilities: messages, view menu 
1. admin login : add new item | delete item | change item price
2. customer : billing | customer name, phone number
3. exit


'''

import sqlite3
import time

connection = sqlite3.connect('menu.db')
cursor = connection.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS Menu([product_id] INTEGER PRIMARY KEY AUTOINCREMENT, 
                [product_name] TEXT, 
                [product_price] INTEGER)''')

query = '''SELECT *  FROM Menu'''
cursor.execute(query)
results = cursor.fetchall()
if results==[]:
    cursor.execute('''
                    INSERT INTO Menu (product_name, product_price)
                    VALUES
                    ('Cake',400),
                    ('Bread',50),
                    ('Cookies',100),
                    ('Doughnuts',80),
                    ('Pie',120)
                    ''')
    connection.commit()


def display_items(cursor):
    query='''SELECT * FROM Menu'''
    cursor.execute(query)
    results=cursor.fetchall()
    print("List of items: ")
    print("ID","Name","Price",sep=" ")
    for each in results:
        print(each[0],each[1],each[2],sep=" ")


def admin_login(connection,cursor):
    print()
    print("---------Welcome! You are logged in as Admin!----------")
    print()
    print("Here are the list of choices:")
    print("Choice 1: Add an item",
            "Choice 2: Remove an item",
            "Choice 3: Update item price",
            "Choice 4: See all the items",
            "Choice 5:Exit",
            sep="\n")

    choice = int(input("Enter your choice: "))
    print()
    time.sleep(0.5)

    if choice==1:
        print("What you like to add?")
        product_name = input("Enter product name: ")
        product_price = input("Enter product price: ")

        try:
            query=f'''INSERT INTO Menu(product_name, product_price) VALUES ('{product_name}','{product_price}')'''
            cursor.execute(query)
            connection.commit()
            print("The item has been added to the list!")
        except Exception as e:
            print("Error occured!")

        time.sleep(1)
        admin_login(connection,cursor)

    elif choice==2:
        display_items(cursor)
        print("Which item you would like to remove?")
        id = int(input("Enter product id:"))
        try:
            query=f'''DELETE FROM Menu WHERE product_id={id}'''
            cursor.execute(query)
            connection.commit()
            print("The item has been removed from the shop!")
        except Exception as e:
            print("Invalid item!")
        time.sleep(1)
        admin_login(connection,cursor)
    elif choice==3:
        display_items(cursor)
        print("Which item price you would like to update?")
        id=int(input("Enter product ID:"))
        price=int(input("Enter the updated price:"))
        try:
            query=f'''UPDATE Menu SET product_price={price} WHERE product_id={id}'''
            cursor.execute(query)
            connection.commit()
            print("The item price has been updated!")
        except Exception as e:
            print("Invalid Product ID!")

        time.sleep(1)
        admin_login(connection,cursor)

    elif choice==4:
        display_items(cursor)
        time.sleep(1.5)
        admin_login(connection,cursor)
    elif choice==5:
        main()
    else:
        print("Invalid Choice!")
        time.sleep(1)
        admin_login(connection,cursor)


def customer_login(connection,cursor):
    print("-----------Welcome,You are logged in as a biller!-------------")
    print("Here is the list of choices:")
    print("Choice 1: Billing", "Choice 2: Exit",sep="\n")
    choice = int(input("Enter your choice:"))
    if(choice==1):
        name = input("Enter the customer name:")
        print(f"What do you wanna buy {name}?")
        time.sleep(0.5)
        display_items(cursor)

        print()
        total = 0
        items=[]
        while 1:

            id=int(input("Enter the product ID:"))
            quantity =int(input("Enter the quantity:"))
            try:
                query=f'''SELECT * FROM Menu WHERE product_id={id}'''
                cursor.execute(query)
                result=cursor.fetchone()
                total += result[2]*quantity
                items.append([result[1],quantity])
                i=input("Anything else?Answer Y for Yes and N for No! ")
                if(i=='N'):
                    break
            except Exception as e:
                print("Invalid Entry!")
                print(e)
                break

        if(total!=0):
            print()
            print("---------Sweet Dough Bakery--------")
            print("-------Billing Details-------")
            print(f"Name:{name}")
            print(f"Items:")
            for each in items:
                print(each[0],each[1],sep=":")
            print(f"Total: {total}")
            print("Thank you! Have a sweet day!")
            print()

        time.sleep(1)
        customer_login(connection,cursor)
    elif choice==2:
        main()
    else:
        print("Invalid Choice!")
        time.sleep(1)
        customer_login(connection,cursor)


def main():
    inloop = 1
    while inloop:
        print()
        print("---------------------------------------------------------------------")
        print("---------------------Welcome to Swweet Dough Bakery!---------------------")
        print("---------------------------------------------------------------------")

        print("How you want to Enter?")
        print("Choice 1: Admin Login","Choice 2: Customer Login", "Choice 3: Exit",sep="\n")


        choice = input("Enter your choice:")
        if choice=='1':
            password = input("Enter the password: ")
            if password=="Arushi":
                admin_login(connection,cursor)
            else:
                print("Incorrect Password!")
                time.sleep(1) 
        elif choice=='2':
            customer_login(connection,cursor)
        elif choice=='3':
            exit()
        else:
            print("Invalid Choice!")
main()
