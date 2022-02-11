import json
import os
import xml.etree.ElementTree as gfg


def GenerateXML(fileName, mylist):
    root = gfg.Element("weather", country="Spain", date="2021-09-25")
    m2 = gfg.Element("summary")
    root.append(m2)
    m1 = gfg.Element("cities")
    root.append(m1)
    for i in mylist:
        b1 = gfg.SubElement(m1, i[0], mean_temp=i[1], mean_wind_speed=i[2], min_temp=i[3], min_wind_speed=i[4], max_temp=i[5],
                            max_wind_speed=i[6])

    tree = gfg.ElementTree(root)

    with open(fileName, "wb") as files:
        tree.write(files)


def read_files():
    mylist = []
    text = ""
    for i in os.scandir("../parsing_serialization_task/source_data"):
        # print(i.name)
        path = "../parsing_serialization_task/source_data/" + i.name
        path = path + "/2021_09_25.json"
        name = i.name
        json1_file = open(path)
        json1_str = json1_file.read()
        json1_data = json.loads(json1_str)
        # print(json1_data)
        # print(json1_data['current'])
        # print(json1_data['hourly']['temp'])
        all_temp = []
        for i in json1_data['hourly']:
            all_temp.append(i['temp'])

        all_wind = []
        for i in json1_data['hourly']:
            all_wind.append(i['wind_speed'])

        a = f'{sum(all_temp) / len(all_temp):.2f}'
        b = f'{sum(all_wind) / len(all_wind):.2f}'
        c = f'{min(all_temp):.2f}'
        d = f'{min(all_wind):.2f}'
        e = f'{max(all_temp):.2f}'
        f = f'{max(all_wind):.2f}'
        mylist.append([name, a, b, c, d, e, f])
    print(mylist)
    GenerateXML("Catalog.xml", mylist)


if __name__ == "__main__":
    read_files()
