import os
folders = input("Please provide list of folder names with spaces in between: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name" + folder)
        break
    except PermissionError:
        break
    print("====Listing files for the folder -" + folder)
    
    for file in files:
        print(file)