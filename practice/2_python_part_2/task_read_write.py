"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os

def read_write(tmp_path):
    mylist = list()
    text = ""
    for filename in os.listdir("../2_python_part_2/files"):
        with open(os.path.join("../2_python_part_2/files", filename), 'r') as f:  # open in readonly mode
            text = text + (f'{f.read()} ')
            mylist.append(str(text))
    print(text)
    with open(tmp_path, 'w', encoding='CP1252') as f:
        fields = text.split(' ')
        f.write(','.join(fields))
