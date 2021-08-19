import os


for named_file in os.listdir(os.getcwd()):
    file_name = named_file
    for letter in file_name:
        if not letter.isalpha():
            file_name = file_name[1:]
        else:
            break
    os.rename(named_file, file_name)
