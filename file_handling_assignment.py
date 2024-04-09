# File Creation
try:
    # Create a new text file named "my_file.txt" in write mode ('w')
    with open("my_file.txt", "w") as file:
        #lines of text to the file
        file.write("This is line 1.\n")
        file.write("12345 is a number.\n")
        file.write("Python is awesome!\n")
    print("File 'my_file.txt' created successfully!")
except PermissionError:
    print("Permission denied to create the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File creation process completed.\n")

# File Reading and Display
try:
    # Open "my_file.txt" in read mode ('r')
    with open("my_file.txt", "r") as file:
        # Read and display the contents of the file
        print("Contents of 'my_file.txt':")
        print(file.read())
except FileNotFoundError:
    print("File 'my_file.txt' not found.")
except PermissionError:
    print("Permission denied to read the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File reading process completed.\n")

# File Appending
try:
    # Open "my_file.txt" in append mode ('a')
    with open("my_file.txt", "a") as file:
        # Append lines of text to the file
        file.write("Appending line 1.\n")
        file.write("Appending line 2.\n")
        file.write("Appending line 3.\n")
    print("Data appended to 'my_file.txt' successfully!")
except PermissionError:
    print("Permission denied to append to the file.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("File appending process completed.")
