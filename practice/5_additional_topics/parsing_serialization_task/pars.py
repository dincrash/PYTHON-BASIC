import os

for i in os.scandir("../parsing_serialization_task/source_data"):
    print(i.name)
