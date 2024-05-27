# file_handling_assignment.py

def create_and_write_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("Line 1: Hello, this is a test.\n")
            file.write("Line 2: The number is 42.\n")
            file.write("Line 3: Python file handling is interesting.\n")
        print("File created and written successfully.")
    except PermissionError:
        print("Permission denied: Unable to write to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print("File not found: Ensure the file exists.")
    except PermissionError:
        print("Permission denied: Unable to read the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def append_to_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Line 4: Appending new content.\n")
            file.write("Line 5: Another line with a number 100.\n")
            file.write("Line 6: End of the file.\n")
        print("File appended successfully.")
    except PermissionError:
        print("Permission denied: Unable to append to the file.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    create_and_write_file()
    read_file()
    append_to_file()
    read_file()

if __name__ == "__main__":
    main()
