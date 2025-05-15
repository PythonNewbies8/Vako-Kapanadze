# ///////////////////////////////////////////////////////////////////////////////////////////////////////

# 1. map() და ლამბდა ფუნქციის გამოყენებით ლისტის თითოეული ელემენტი აიყვანეთ კბვადრატში
# listi = [2, 3, 4, 5]
# kvadrati = map(lambda num: num ** 2, listi)
# print(list(kvadrati))

# ///////////////////////////////////////////////////////////////////////////////////////////////////////

# # 2. filter() და ლამბდას გამოყენებით დააბრუნეთ ლისტიდან ყველა ის რიცხვი, რომელიც კენტია
# listi = [2, 3, 4, 5, 6]
# odd = filter(lambda x: x % 2 == 1,listi)
# print(list(odd))
# 3.აღწერეთ map(), reduce(), filter(), zip(), ანუ რა უნდა გადავცეთ, სინტაქსი....
# map(ფუნქცია, მონაცემთა სიმრავლე(ლისტი, თაფლი, დიქტი, სეტი და სტრინგი)) დაბეჭვდისას უნდა გადავცეთ მონაცემთა ტიპი რომელშიც უნდა დაბეჭდოს საბოლოო შედეგი.

# reduce() მუშაობის პრინციპი :
# #  იღებს მონაცემთა სიმრავლის პირველ ორ ელემენტს ფუნქციას იყენებს მათზე და შედეგს აბრუნებს
# შედეგი + შემდეგი ელემენტი → ისევ ფუნქცია და ასე გრძელდება ბოლომდე Syntax ==> from functools import reduce || reduce(function, iterable)

# filter(): ფილტრავს ელემენტს მონაცემთა სიმრავლიდან იმის მიხედვით რა ლოგიკაც ფუნქციაშია მიწოდებული:
# filter(function, iterable) აბრუნებს True ან False-ს და ტოვებს მხოლოდ იმ ელემენტს რომლებიც არიან True (სჭრიდება ამობეჭვდისას გადავცეთ მონაცემთა ტიპი რომელშიც უნდა დაბეჭდოს შედეგი)

# zip(): ორ ან რამდენიმე მონაცემთა სიმრავლეს ინდექსების მიხედვით აჯგუფებს წყვილებად ან ტრიპლეტებად ან ოთხლეტებად და ა.შ || zip(iterable1, iterable2, ...) 
# p.s ქმნის თაფლის სიმრავლეს წყვილებად

# ///////////////////////////////////////////////////////////////////////////////////////////////////////
# # 5. მეპის, რენდომ მოდულისა და ლამბდას გამოყენებით დაწერეთ პროგრამა, რომელიც არსებულ ლისტში მოცემულ ქულებს უმატებს რენდომად შერჩეულ რიცხვს(1-დან 100-მდე).
# # (ლისტი წინასწარ განსაზღვრეთ თქვენით)
# import random
# listi = [2, 3, 4, 5, 6, 7, 8]
# func = map(lambda x: x + random.randint(1,100), listi)
# print(list(func))

# ///////////////////////////////////////////////////////////////////////////////////////////////////////

# 6. დააგენერირეთ რენდომ ელემენტებისგან(ინტეჯერებისგან) შემდგარი 5 ელემენტიანი ლისტი.
# გამოიყენეთ გამონაკლისები და სთხოვეთ იუზერს შემოიყვანოს ინდექსი და იმის მიხედვით დაუბრუნეთ შესაბამისი ელემენტი.
# (ერორის ტიპები: IndexError, ValueError)
# import random

# listi = [random.randint(1, 999) for num in range(1, 6)]
# answer = input("Enter index to find out which number is on that index: ")

# try:
#     index = int(answer)
#     if index < 0:
#         raise IndexError("Our program does not know how to handle negative index numbers yet, please wait for an update.")
#     elif index >= len(listi):
#         raise IndexError("Index is out of range, please enter from 0-4 only.")
    
#     print(f"{index} Indexze aris ricxvi: {listi[index]}")

# except IndexError as ie:
#     print(ie) 
# except ValueError:
#     print("Incorrect value, please enter only integers.")

# ///////////////////////////////////////////////////////////////////////////////////////////////////////

import sys
# user_balances = {
#     "Dean": 20000,
#     "John": 15000,
#     "Bryan": 1500
# }

# def check_balance():
#     try:
#         name = input("Please enter a name of the client: ").title()

#         if not name.isalpha():
#             raise TypeError("Name must contain only alphabetical letters.")
#         if name not in user_balances:
#             raise KeyError("This client does not exist in the database.")
        
#         balance = user_balances[name]
#         print(f"User Balance: {name}: {balance}$")
#     except TypeError as te:
#         print(te)
#     except KeyError as ke:
#         print(ke)

# def deposit():
#     try:
#         name = input("Please enter a name of the client: ").title()
    
#         if not name.isalpha():
#             raise TypeError("Name must contain only alphabetical letters.")
#         if name not in user_balances:
#             raise KeyError("This client does not exist in the database.")
        
#         amount = input(f"User Balance: {name}: {user_balances[name]}$ How much do you want to deposit? ")

#         if not amount.isdigit():
#             raise ValueError("Deposit amount must be a valid number.")
        
#         amount = int(amount) 

#         if amount <= 0:
#             raise ValueError("Deposit amount must be a positive number.")
        
#         user_balances[name] = user_balances[name] + amount

#         print(f"You successfully Deposited {amount}$ and user's new balance is: {name}: {user_balances[name]}$")
    
#     except ValueError as ve:
#         print(ve)
#     except TypeError as te:
#         print(te)
#     except KeyError as ke:
#         print(ke)

# def withdraw():
#     try:
#         name = input("Please enter a name of the client: ").title()
    
#         if not name.isalpha():
#             raise TypeError("Name must contain only alphabetical letters.")
#         if name not in user_balances:
#             raise KeyError("This client does not exist in the database.")
        
#         amount = input(f"User Balance: {name}: {user_balances[name]}$ How much do you want to withdraw? ")

#         if not amount.isdigit():
#             raise ValueError("Withdraw amount must be a valid number.")
        
#         amount = int(amount) 

#         if amount <= 0:
#             raise ValueError("Withdraw amount must be a positive number.")

#         if amount > user_balances[name]:
#             raise ValueError("Insufficient funds to complete the withdrawal.")
        
#         user_balances[name] = user_balances[name] - amount

#         print(f"You successfully Withdrawn {amount}$ and user's new balance is: {name}: {user_balances[name]}$")
    
#     except ValueError as ve:
#         print(ve)
#     except TypeError as te:
#         print(te)
#     except KeyError as ke:
#         print(ke)

# def main():
#     while True:
#         answer = input("""Please choose an operation below:
#         1. Check balance
#         2. Deposit
#         3. Withdraw
#         4. Exit
#         """)
#         if answer == "1":
#             check_balance()
#         elif answer == "2":
#             deposit()
#         elif answer == "3":
#             withdraw()
#         elif answer == "4":
#             print("Exiting the program. Goodbye!")
#             sys.exit()
#         else:
#             print("Invalid choice. Please choose 1-4.")

# if __name__ == "__main__":
#     main()

# ///////////////////////////////////////////////////////////////////////////////////////////////////////


# ამოცანა: მოსწავლეთა ქულების დამუშავება
# მიზანი: დაწერეთ პითონის პროგრამა, რომელიც ამუშავებს მოსწავლეთა შეფასებებს map(), filter(), zip() და reduce() გამოყენებით.

# ეტაპები
# - შექმენით მოსწავლეთა სახელების სია და მათი შეფასებების შესაბამისი სია.
# - გამოიყენეთ zip() სახელებისა და კლასების  გაერთიანებისთვის.
# - გამოიყენეთ map(), რომელიც ციფრებს(A-90-100...)  ასოებად გარდაქმნის.
# -  გამოიყენეთ filter() იმ სტუდენტების საპოვნელად, რომლებმაც ჩააბარეს (მაგ., ქულა ≥ 50).
# -  გამოიყენეთ reduce() საშუალო კლასის შეფასების გამოსათვლელად.
# from functools import reduce
# students = ["Peter", "Bryan", "Lois", "Clevlend", "Meg"]
# grades = [48, 90, 95, 55, 42]
# def zipping(students, grades):
#     return list(zip(students, grades))
# listi = zipping(students,grades)
    
# def convert_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     elif score >= 50:
#         return "E"
#     else:
#         return "F"
# letter_grades = list(map(convert_grade, grades))
# def filter_students(listi):
#     return list(filter(lambda pair: pair[1] >= 50, listi))
# passed = filter_students(listi)
# def reduce_students(grades):
#     summ = reduce(lambda x,y: x + y, grades)
#     average = summ / len(grades)
#     return average
# reduced = reduce_students(grades)
# def main():
#     answer = input(""" Enter only number:
#     1. Zip
#     2. Map
#     3. Filter
#     4. Reduce
#     """)

#     if answer == "1":
#         print(listi)
#     elif answer == "2":
#         print(letter_grades)
#     elif answer == "3":
#         print(passed)
#     elif answer == "4":
#         print(reduced)
# if __name__ == "__main__":
#     main()

