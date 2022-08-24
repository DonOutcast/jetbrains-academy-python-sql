import random
import sqlite3 as sq


class Database:
    """For database"""
    def __init__(self, name: str) -> None:
        self.name = name
        self.base = sq.connect(f"{self.name}")
        self.cur = self.base.cursor()

    def create_table_complex(self):
        if self.base:
            query = """CREATE TABLE IF NOT EXISTS 
                        card (id INTEGER PRIMARY KEY AUTOINCREMENT,      
                                 number TEXT,
                                 pin TEXT,
                                 balance INTEGER DEFAULT 0
                                 )"""
            self.cur.execute(query)
            self.base.commit()

    def add_information(self, card_number, card_pin):
        query = """INSERT INTO card (number, pin) VALUES (
        ?,?)"""
        self.cur.execute(query, (card_number, card_pin))
        self.base.commit()

    def check_user(self, card_number, card_pin):
        print(card_pin)
        query = """SELECT pin FROM card WHERE number=?"""
        check_pin = self.cur.execute(query, (card_number,)).fetchone()
        if check_pin is not None:
            return card_pin == check_pin[0]
        else:
            return False
    def get_balance(self, card_number):
        query = """SELECT balance FROM card WHERE number=? """
        get = self.cur.execute(query, (card_number,)).fetchone()
        self.base.close()
        return get





class Bank:
    """Simple Banking system"""

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_menu() -> int:
        """This is  function print menu"""
        menu = ("1. Create an accounti", "2. Log into account", "0. Exit")
        menu = "\n".join(num for num in menu)
        print(menu)
        user_input = int(input())
        return user_input

    @staticmethod
    def gen_numbers_of_card() -> str:
        """This is function generation numbers for bank cards"""
        number_one = "4"
        number_two_seven = "00000"
        number_last = 0
        account_number = str(random.randint(0, 999999999)).zfill(9)
        card_number = number_one + number_two_seven + account_number
        check_card_numbers = list(int(i) for i in card_number)
        temp = 0
        for j in range(len(check_card_numbers)):
            if j % 2 == 0 and check_card_numbers[j] != 0:
                check_card_numbers[j] *= 2
            if check_card_numbers[j] > 9:
                check_card_numbers[j] -= 9
            temp += check_card_numbers[j]
        if temp % 10 != 0:
            number_last = 10 - temp % 10
        card_number += str(number_last)
        return card_number

    @staticmethod
    def gen_password() -> str:
        """This is function generation password"""
        password = str(random.randint(0, 9999)).zfill(4)
        return password

    @staticmethod
    def get_log() -> list:
        """This is a function output card and password for log"""
        your_input = []
        print("Enter your card number:")
        your_input.append(input())
        print("Enter your PIN:")
        your_input.append(input())
        return your_input

    @staticmethod
    def get_log_menu() -> int:
        log_menu = ("1. Balance", "2. Log out", "0. Exit")
        print("\n".join(log_menu))
        user_input = int(input())
        return user_input


user_db = Database("card.s3db")
user_db.create_table_complex()
cards = []
passwords = []
answer = 1
new_user = Bank("Shamil")
answer = new_user.get_menu()
while answer != 0:
    if answer == 1:
        new_card = new_user.gen_numbers_of_card()
        if new_card not in cards:
            cards.append(new_card)
            passwords.append(new_user.gen_password())
            user_db.add_information(cards[-1], passwords[-1])
            print("Your card has been created")
            print(f"Your card number:\n{cards[-1]}")
            print(f"Enter your PIN:\n{passwords[-1]}")
    elif answer == 2:
        check = new_user.get_log()
        # print(user_db.check_user(check[0], check[1]), "seeee <<<<<")
        if not user_db.check_user(check[0], check[1]):
            print("Wrong card number or PIN!")
        else:
            print("You have successfully logged in!")
            log_answer = new_user.get_log_menu()
            if log_answer == 1:
                val = user_db.get_balance(check[0])
                print(val[0])
            elif log_answer == 2:
                print("You have successfully logged out!")
            else:
                break
    answer = new_user.get_menu()
else:
    print("Bye!")

