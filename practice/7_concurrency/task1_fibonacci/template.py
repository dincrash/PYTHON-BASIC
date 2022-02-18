import os
from random import randint
import re
from multiprocessing import Pool

OUTPUT_DIR = './output'
RESULT_FILE = './result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list):
    with Pool(200) as p:
        p.map(writefile, array)


def writefile(i):
    result = fib(i)
    save_path = "output/"
    complete_name = os.path.join(save_path, str(i) + ".txt")
    with open(complete_name, 'w', encoding='CP1252') as f:
        f.write(str(result))


def func2(result_file: str):
    mylist = []
    out = []
    text = ""
    for filename in os.listdir("output"):
        with open(os.path.join("output", filename), 'r',
                  encoding='CP1252') as f:
            text = text + f'{f.read()} '
        mylist.append(re.sub('[.txt]', '', str(filename)))
        mylist.append(str(text))
        out.append(mylist)
        mylist = []
        text = ""
    with open(result_file, 'w', encoding='CP1252') as f:
        for i in out:
            output = (str(i[0]) + " " + str(i[1]) + "\n")
            fields = output.split(' ')
            f.write(','.join(fields))


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    func1(array=[randint(1000, 100000) for _ in range(1000)])
    func2(result_file=RESULT_FILE)
