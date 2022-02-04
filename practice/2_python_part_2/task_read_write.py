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
mylist = list()
text = ""
for filename in os.listdir("files"):
   with open(os.path.join("files", filename), 'r') as f: # open in readonly mode
       text = text + (f'{f.read()} ')
       mylist.append(str(text))
print(text)
with open('result.txt', 'w', encoding='CP1252') as f:
    fields = text.split(' ')
    f.write(','.join(fields))