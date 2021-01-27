import logging

# file operations
# from time import sleep
#
# file = open("my_text", "w")
# file.write('New text')
# file.close()
#
# # print(type(file))
# sleep(3)
#
# with open("my_text", "w") as file2:
#     file2.write('New text 2')


class FileWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.file = open(self.file_path, 'x')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.write('\n')
        self.file.write(str(exc_tb.tb_frame).split(',', 1)[1])
        self.file.close()
        return True


with FileWriter("new_file") as file:
    my_string = int(input(">>>"))
    while my_string:
        my_string2 = input("...")
        file.write(str(my_string) + ("\n" if my_string2 else ""))
        my_string = int(my_string2)
