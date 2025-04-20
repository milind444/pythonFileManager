import os

def create_name(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename} created successfully")
    except FileExistsError:
        print(f"File Name {filename} already exists")

    except Exception as e:
        print('An error occurred')

def view_all_files():
    files=os.listdir()
    if not files:
        print('no files found')
    else:
        print('files found in directory')
        for file in files:
            print(file)
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted successfully')
    except FileNotFoundError:
        print("file not found")
    except Exception as e:
        print("an error occurred!!!")

def read_file(filename):
    try:
        with open('sample.txt','r') as f:
            content=f.read()
            print(f"content of '{filename}' : \n{content}")
    except FileNotFoundError:
        print('file not found!')
    except Exception as e:
        print('An error occurred')

def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content=input('enter data to add')
            f.write(content+'\n')
            print('content added to {filename} successfully!!!')
    except FileNotFoundError:
        print(f'{filename} not found')
    except Exception as e:
        print('An error occuerred!!!')

def main():
    while True:
        print('File Management App')
        print('1. Create file')
        print('2. View all files')
        print('3. Delete file')
        print('4. Read file')
        print('5. Edit file')
        print('6. Exit')

        choice=input('Enter your choice(1-6)=')

        if choice == '1':
            filename=input("Enter the file-name to create=")
            create_name(filename)
        elif choice=='2':
            view_all_files()
        elif choice == '3':
            filename=input('Enter the name of the file you want to delete:')
            delete_file(filename)
        elif choice == '4':
            filename=input('Enter the name of the file you want to read:')
            read_file(filename)
        elif choice == '5':
            filename=input('Enter the name of the file you want ot edit:')
            edit_file(filename)
        elif choice == '6':
            print('closing the app...')
            break
        else:
            print('Invalid syntax')

if __name__=="__main__":
    main()