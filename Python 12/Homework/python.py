# # დავალება: ფაილის ხაზების შებრუნება           
# # __________________________________________|

# # სთხოვეთ მომხმარებელს შეიყვანოს ფაილის სახელი. საბოლოოდ, 

# # - წაიკითხეთ ყველა სტრიქონი(ხაზი) ფაილიდან.
# # - თითოეულ ხაზში შეაბრუნეთ სიმბოლოები (ანუ წყობა გახდეს მარჯვნიდან მარცხნივ -> hello -> olleh).
# # - გამოიყენეთ seek(0) დასაწყისში გადასასვლელად.
# # - გადაწერეთ ფაილი შებრუნებული ხაზებით.
# # - დაამუშავეთ შეცდომები
# # - მიიღეთ ახალი ფაილი აღნიშნული წყობით

# def main():
#     inp_name = input("Please enter file name: ")
#     file = f"C:/Users/vakok/OneDrive/Desktop/{inp_name}"
#     open_file(file)
#     copy_file(file, "C:/Users/vakok/OneDrive/Desktop/new.txt")

# def open_file(filename):
#     try: 
#         with open(filename, "r+") as f:
#             content = f.readlines() 
#             print(content) 
#     except FileNotFoundError:
#         print("You entered a wrong file name")
#     except Exception as e:
#         print(f"Error {e}")

# def copy_file(saidan, sad):
#     try:
#         with open(saidan, "r+") as dest:
#             content = dest.readlines()  
#             dest.seek(0)  
#             for word in content[::-1]: 
#                 dest.write(word.strip()[::-1] + "\n") 
#             dest.seek(0)  
#             readit = dest.read() 
#             print("Content after writing and reading back:")
#             print(readit)
        
#         with open(sad, "w") as new_file:
#             new_file.write(readit) 

#     except FileNotFoundError:
#         print("Error: Source file not found.")
#     except Exception as e:
#         print(f"Error {e}")

# if __name__ == "__main__":
#     main()

import sys
SESSION_FILE = 'C:/Users/vakok/OneDrive/Desktop/session.txt'
USERS = {'ann':'password123', 'amm':'pass123'}
# login(), logout(), is_logged_in(), current_user()

def login(username, password):
    if USERS.get(username) == password:
        try:
            f = open(SESSION_FILE, 'w')
            f.write(username)
            f.close()
            print(f'logged in as {username}')
        except Exception as e:
            print(f'error {e}') 
    else:
        print('invalid credential')

def signup(username, password):
    try:
        if username not in USERS:
            USERS[username] = password
            print(f'User {username} signed up successfully.')

            f = open(SESSION_FILE, 'w')
            f.write(username)  
            f.close()
        else:
            print('Username already exists.')
    except Exception as e:
        print(f'error {e}')

def logout():
    try:
        f = open(SESSION_FILE, 'w')
        f.write('')
        f.close()
        print('logged out successfully')
    except Exception as e:
        print(f'error {e}')

def is_logged_in():
    try:
        f = open(SESSION_FILE, 'r')
        logged = bool(f.read().strip())
        f.close()
        return logged
    except Exception as e:
        print(e)

def current_user():
    try:
        f = open(SESSION_FILE, 'r')
        user = f.read().strip() or None
        f.close()
        return user
    except Exception as e:
        print(e)

if __name__ == '__main__':
    while True:
        print('1. login')
        print('2. logout')
        print('3, current user')
        print('4. Sign Up')
        print('5. exit ')
        
        choice = input("choose ")

        if choice == '1':
            username = input('username ')
            password = input('password ')
            login(username, password)
        
        elif choice == '2':
            logout()

        elif choice == '3':
            user = current_user() 
            print(f'logged in as {user}' if user else 'not user found')
        
        elif choice == '4':
            username = input('username ')
            password = input('password ')
            signup(username, password)

        elif choice == '5':
            sys.exit()

        else:
            print('not valid choice, try again ')
