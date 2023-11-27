# 1. Create a Python script that does the following:
# Takes a directory path and a file extension as command line arguments (use sys.argv).
# Searches for all files with the given extension in the specified directory (use os module).
# For each file found, read its contents and print them.
# Implement exception handling for invalid directory paths, incorrect file extensions, and file access errors.

# Ex 1
import os
import sys

def read_and_print_files(directory_path, file_extension):
    try:
        if not os.path.exists(directory_path):
            raise FileNotFoundError("Directory not found.")
        files = [file for file in os.listdir(directory_path) if file.endswith(file_extension)]
        if not files:
            raise FileNotFoundError(f"No files with extension '{file_extension}' found in the directory.")
        for file_name in files:
            file_path = os.path.join(directory_path, file_name)
            try:
                with open(file_path, 'r') as file:
                    print(f"Contents of '{file_name}':")
                    print(file.read())
                    print("-" * 30)
            except Exception as e:
                print(f"Error reading '{file_name}': {str(e)}")
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         print("Usage: python script.py <directory_path> <file_extension>")
#     else:
#         directory_path = sys.argv[1]
#         file_extension = sys.argv[2]
#         read_and_print_files(directory_path, file_extension)



# 2. Write a script using the os module that renames all files in a specified directory to have a sequential number prefix. 
# For example, file1.txt, file2.txt, etc. Include error handling for cases like the directory not existing or files that can't be renamed.

# Ex 2
def ex2():
    dir = "D://Python//Folder"
    try:
        if not os.path.exists(dir):
            raise FileNotFoundError(dir + " not found")
        files = os.listdir(dir)
        for file in files:
            if os.path.isfile(os.path.join(dir, file)):
                number = 1
                for file in files:
                    source = dir + "//" + file
                    index = file.rfind('.')
                    dest = dir + "//" + file[:index] + str(number) + file[index:]
                    try:
                        os.rename(source, dest)
                    except FileNotFoundError:
                        print(file, "not found.")
                    except OSError:
                        print(file, "could not be renamed")
                    number += 1
    except FileNotFoundError as e:
        print(e)
ex2()



# 3. Create a Python script that calculates the total size of all files in a directory provided as a command line argument. 
# The script should:
# Use the sys module to read the directory path from the command line.
# Utilize the os module to iterate through all the files in the given directory and its subdirectories.
# Sum up the sizes of all files and display the total size in bytes.
# Implement exception handling for cases like the directory not existing, permission errors, or other file access issues.

# Ex 3
def ex3(dir):
    try:
        if not os.path.exists(dir):
            raise FileNotFoundError(dir + " not found.")
        total_size = 0
        for (root, directories, files) in os.walk(dir):
            for file in files:
                try:
                    total_size += os.path.getsize(os.path.join(root, file))
                except PermissionError:
                    print("Permission denied on", file)
                except Exception as e:
                    print(str(e))
        print("The total size is", total_size, "bytes.")
    except FileExistsError as e:
        print(e)
    except Exception as e:
        print(str(e))

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Please provide a directory path")
#     else:
#         ex3(sys.argv[1])



# 4. Write a Python script that counts the number of files with each extension in a given directory. The script should:
# Accept a directory path as a command line argument (using sys.argv).
# Use the os module to list all files in the directory.
# Count the number of files for each extension (e.g., .txt, .py, .jpg) and print out the counts.
# Include error handling for scenarios such as the directory not being found, no read permissions, or the directory being empty.

# Ex 4

def ex4(dir):
    try:
        if not os.path.exists(dir):
            raise FileNotFoundError(dir + " not found.")
        ext_counts = {}
        try:
            if len(os.listdir(dir)) == 0:
                raise Exception("No files in this folder.")
            for fis in os.listdir(dir):
                if os.path.isfile(os.path.join(dir, fis)):
                    ext = os.path.splitext(fis)[-1]
                    if ext in ext_counts.keys():
                        count = ext_counts[ext]
                    else:
                        count = 0
                    count += 1
                    ext_counts[ext] = count
            print(ext_counts)
        except PermissionError:
            print("Permission denied on", dir)
        except Exception as e:
            print(str(e))
    except FileExistsError as e:
        print(e)

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Please provide a directory path")
#     else:
#         ex4(sys.argv[1])