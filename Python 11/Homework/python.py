# def create(filename):
#     with open(filename, "w") as f:
#         f.write("10\n2")

# def read_numbers(filename):
#     with open(filename, "r+") as f:
#         try:
#             lines = f.readlines()
#             num1 = int(lines[0])
#             num2 = int(lines[1])
#             return num1 / num2
#         except ZeroDivisionError:
#             print("Zero Division Error, please select a different number.")
#             return None
#         except IndexError:
#             print("File doesn't contain two numbers.")
#             return None
#         except ValueError:
#             print("File contains non-integer values.")
#             return None

# file_path = "C:/Users/vkapanadze/Desktop/file.txt"
# create(file_path)
# print(read_numbers(file_path))

# ////////////////////////////////////////////////////////////////////
# 2 - გაქვთ ფაილი რომელიც შეიცავს გარკვეულ მონაცემებს(ანუ ჩანაწერს :) ), დააკოპირეთ მასში არსებული კონტენტი სხვა destination.txt ფაილში,
# რომელიც აუცილებლად დესკტოპზე უნდა იყოს.
def copy_file(saidan, sad):
    with open(saidan, "r") as src:
        content = src.read()
    with open(sad, "w") as dest:
        dest.write(content)
    print("File copied successfully.")
copy_file("C:/Users/vkapanadze/Desktop/file.txt","C:/Users/vkapanadze/Desktop/NewFile.txt")
# ////////////////////////////////////////////////////////////////////
# N3 --
# def write_lines(filename):
#     with open(filename, "w") as f:
#         f.write("line 1\n")
#         f.write("line 2\n")
#         f.write("line 3\n")
#         f.write("line 4\n")

# def counter(filename):
#     try:
#         with open(filename, "r") as f:
#             count = 0
#             lines = f.readlines()
#             for line in lines:
#                 count += 1
#             return count
#     except FileNotFoundError:
#         print("File was not found")
#         return None

# file_path = "C:/Users/vkapanadze/Desktop/file.txt"
# write_lines(file_path)
# print(counter(file_path))

# ////////////////////////////////////////////////////////////////////
# 4 --
# user_input = input("Enter names separated by commas: ").split(",")
# def lineup(input_data, filename):
#     try:
#         # Add newline to each item
#         formatted = [name.strip() + "\n" for name in input_data]
#         with open(filename, "w") as f:
#             f.writelines(formatted)
#         # Re-open file for reading lines
#         with open(filename, "r") as f:
#             lines = f.readlines()
#             print("Written lines:", lines)
#     except IOError:
#         print("An IOError occurred while accessing the file.")

# file_path = "C:/Users/vkapanadze/Desktop/file.txt"
# lineup(user_input, file_path)

# ////////////////////////////////////////////////////////////////////
# 5 - მოითხოვეთ იუზერისგან ფაილის სახელი, რომლის გახსნაც სურს (ამ შემთხვევაში path აირჩიეთ თქვენი დესკტოპი ან ნებისმიერი დირექტორია):
#         | გახსენით ფაილი r+ მოუდში.
#         | დაპრინტეთ პირველი 20 სიმბოლო
#         | გამოიყენეთ seek(0) და დაბრუნდით ფაილის დასაწყისში
#         | გადააწერეთ პირველ ხაზს "modified content"
# def open_content(path):
#     try:
#         with open(path, "r") as f:
#             content = f.read()
#             print(content)
#     except FileNotFoundError:
#         print("File not found. Please check the name and try again.")
#     except IOError:
#         print("There was a problem opening the file.")

# def read_symbols(path):
#     try:
#         with open(path, "r") as f:
#             content = f.read(20)
#             print(content)
#     except FileNotFoundError:
#         print("File not found. Please check the name and try again.")
#     except IOError:
#         print("There was a problem opening the file.")

# def modify_first_line(path):
#     try:
#         with open(path, "r") as f:
#             lines = f.readlines()
#         if lines:
#             lines[0] = "Modified Content\n"
#         else:
#             print("File is empty. Cannot modify first line.")
#         with open(path, "w") as f:
#             f.writelines(lines)
#         print("File updated successfully.")
#     except FileNotFoundError:
#         print("File not found. Please check the name and try again.")
#     except IOError:
#         print("There was a problem opening or writing in the file.")

# def main(file_path):
#     if not file_path:
#         print("Invalid file path.")
#         return
#     open_content(file_path)
#     read_symbols(file_path)
#     modify_first_line(file_path)
#     print("Task completed.")

# if __name__ == "__main__":
#     filename = input("Enter the file name: ")
#     file_path = f"C:/Users/vkapanadze/Desktop/{filename}"
#     main(file_path)


