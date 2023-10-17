def Uppercase(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.upper(), end='')
    except FileNotFoundError:
        print (f" File '{file_name}' not found. Enter valid file.")
file_name=input("Enter the file name: ")        
Uppercase(file_name)