# # # with open() as f -- context manager - avtomaturad daxurva 

f = open('C:/Users/PC/Desktop/norm.txt' , 'w')
f.write('hello world')
f.close()  # file davxure - aucileblad 

# # print('hello')



# # ////////////////////////////////////////////////////////////////////////////////////////////////

# def count_words(filename):
#     try:
#         with open(filename, 'r', encoding='utf-8') as f:
#             text = f.read()
#             words = text.split()   # [words, words, word...]
#             return len(words)
#     except FileNotFoundError:
#         print('file not found')
#         return 0
    

# def count_characters(filename):   
#     try:
#         with open(filename, 'r', encoding='utf-8') as f:
#             text = f.read()
#             text = text.replace(' ', '')   #spacebit roar datvalos 
#             return len(text)
#     except FileNotFoundError:
#         print('file not found')
#         return 0

# file_path = 'C:/Users/PC/Desktop/norm.txt'
# print('word count', count_words(file_path))
# print('char count', count_characters(file_path))

    
# # /////////////////////////////////////////////////////////////////////////////////////////////////////////
# import sys
# # davalebad sign up-is damateba 
# def main():
#     while True:
#         print('1. login')
#         print('2. logout')
#         print('3, current user')
#         print('4. exit ')
#         choice = input("choose ")

#         if choice == '1':
#             username = input('username ')
#             password = input('password ')
#             login(username, password)
        
#         elif choice == '2':
#             logout()

#         elif choice == '3':
#             user = current_user()   #true an false   - if user
#             print(f'logged in as {user}' if user else 'not user found')

#         elif choice == '4':
#             sys.exit()

#         else:
#             print('not valid choice, try again ')


# SESSION_FILE = 'C:/Users/PC/Desktop/session.txt'
# USERS = {'ann':'password123', 'amm':'pass123'}
# # login(), logout(), is_logged_in(), current_user()

# def login(username, password):
#     if USERS.get(username) == password:
#         try:
#             with open(SESSION_FILE, 'w') as f:
#                 f.write(username)
#             print(f'logged is as {username}')

#         except Exception as e:
#             print(f'error {e}') 
#     else:
#         print('invalid credential') 

# def logout():
#     # del 
#     try:
#         with open(SESSION_FILE, 'w') as f:
#             f.write('')
#         print('logged out succesfully')
#     except Exception as e:
#             print(f'error {e}')

# def is_logged_in():
#     try:
#         with open(SESSION_FILE, 'r') as f:
#             return bool(f.read().strip()) # tu file carieli araa -true, sxva shemtxvevashi false    bool(0) bool(1)
#     except Exception as e:
#         print(e)

# def current_user():
#     try:
#         with open(SESSION_FILE, 'r') as f:
#             return f.read().strip() or None
#     except Exception as e:
#         print(e)


# if __name__ == '__main__':
    # main()
#     while True:
#         print('1. login')
#         print('2. logout')
#         print('3, current user')
#         print('4. exit ')
#         choice = input("choose ")

#         if choice == '1':
#             username = input('username ')
#             password = input('password ')
#             login(username, password)
        
#         elif choice == '2':
#             logout()

#         elif choice == '3':
#             user = current_user()   #true an false   - if user
#             print(f'logged in as {user}' if user else 'not user found')

#         elif choice == '4':
#             sys.exit()

#         else:
#             print('not valid choice, try again ')
        

# print(__name__ == '__main__')


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# 0, 1  // 8 bit = 1 byte

# # mp3, mp4, jpg, jpeg, png , pdf
# # pillow // image

# # bytebis ukan gadmotargmna
# # def read_image_bytes(filename, num_bytes = 29):
# #     with open(filename, 'rb') as f:    # rb kitxulobs binarul filebs 
# #         data = f.read(num_bytes)
# #         print(data)
# # read_image_bytes('pic.png')

# # ////////////////////////////////////////////////////////////////////////////////////

# def copy_binary_files(src_path, destination_path):
#     try:
#         with open(src_path, 'rb') as src_file:
#             data = src_file.read()
#             print(data)

#         with open(destination_path, 'wb') as dest_file:
#             dest_file.write(data)
#         print('file copied')
#     except Exception as e:
#         print(e)

# copy_binary_files('pic.png', 'image.png')


# def copy_binary_files(src_path):
#     try:
#         with open(src_path, 'rb') as src_file:
#             data = src_file.read()
#             # print(data)

#         # with open(destination_path, 'wb') as dest_file:
#         #     dest_file.write(data)
#         # print('file copied')
#     except Exception as e:
#         print(e)

# copy_binary_files('session.txt')




# GIORGI--- https://stackoverflow.com/questions/14759637/python-pil-bytes-to-image