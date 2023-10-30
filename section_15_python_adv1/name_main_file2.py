import name_main_file1

print("Top level file2")
name_main_file1.func()

if __name__ == "__main__":
    print("File2 called directly")
else:
    print("File2 has been imported")