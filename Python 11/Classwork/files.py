
# # წაკითხვა, დაკოპირება, წაშლა, ჩასმა, გადატანა, დამატება   ...

# # გავხსნა, წაკითხვა, ჩავწერა, დამატება, წაშლაც, ფაილის დახურვა

# # gaxsna - wakitxva

# # r"C:\Users\PC\Desktop\leqcia.txt"
# # /
# # \\ - sawyisii 
#     # .read()
#     # content = f.read() mtlians

#     # content = f.readline()  xazebs
#     # content2 = f.readline()

#     # print(content, content2)
#     # line = f.readline()
#     # # while line:
#     # #     print(line, end = '')
#     # #     line = f.readline()
#     # for i in range(5):
#     #     print(line)
#         # line = f.readline()

# input
# with open("C:/Users/PC/Desktop/{leqcia.txt}", 'r+') as f:   # seek() 
#     content = f.read()
#     print(content)

#     f.seek(0)
#     f.write("new data ")

#     f.seek(0)
#     print('after writing ', f.read())


# ////////////////////////////////////////////////////////////////////
# filenotfounderror
# permissionError
# Exception 
# def read_mode():

#     try:
#         with open("C:/Users/PC/Desktop/titanic.json", 'r') as f:
#             content = f.read()
#             print(content)
#     except FileNotFoundError:
#         print('not found')

#     except PermissionError:
#         print('permission')

#     except Exception as e:
#         print(e)

# read_mode()

# ////////////////////////////////////////////////
# #  tu ararsebobs qmnis, tu arsebobs zemodaan awers....
# try:
#     with open("C:/Users/PC/Desktop/leqjahybdjhacia.txt", 'w') as f:
#         f.write("tsdcvsdcdshis is added new wejhyfwjehbcf")  #gadawera 
#     print('added sucessfully')
# except Exception as e:
#     print(e)

# ///////////////////////////////////////


# try:
#     with open("C:/Users/PC/Desktop/leqjahybdjhacia.txt", 'a') as f:
#         f.write("\n   newly added")  #damateba 
#     print('appended sucessfully')
# except Exception as e:
#     print(e)
    # ////////////////////////////////////////

# 'w' write()  writeline() writelines()

# def write_lines():

#     lines = ['line 1\n', 'line2\n', 'srtingi']
#     with open("C:/Users/PC/Desktop/lines.txt", 'w') as file:
#         file.writelines(lines)
#     print('works correclty')
# write_lines()

# //////////////////////////////////////////////


# def insert_line():
#     try:
#         with open("C:/Users/PC/Desktop/lines.txt") as f:
#             lines = f.readlines()

#         lines.insert(1, 'this is inserted\n')
#         lines.insert(5, 'this is inserted\n')

#         with open("C:/Users/PC/Desktop/lines.txt", 'w') as f:
#             f.writelines(lines)

#         print('updated')

#     except:
#         print('not working') 
   

# insert_line()

# ///////////////////////////////////////////////

# washla
with open("C:/Users/PC/Desktop/lines.txt") as f:
    lines = f.readlines()
del lines[1]
with open("C:/Users/PC/Desktop/lines.txt", 'w') as f:
    f.writelines(lines)

# ///////////////////////////////////////////////////


# input
# with open(f"C:/Users/PC/Desktop/{input}", 



