import json
import os
import xml.etree.ElementTree as gfg
from typing import Dict


def GenerateXML(fileName, mylist):
    root = gfg.Element("weather", country="Spain", date="2021-09-25")
    summary = []
    allsummary = []
    b = 0
    c = 1

    while c < 3:
        while b < (len(mylist) - 1):
            b = b + 1
            summary.append(float(mylist[b][c]))
        allsummary.append(f'{(sum(summary) / len(mylist)):.2f}')
        summary.clear()
        b = 0
        c = c + 1

    b = 0
    coldest = []
    while b < (len(mylist) - 1):
        coldest.append(mylist[b][3])
        b = b + 1
    i = (min(coldest))
    # print(mylist[3])
    cold = list(coldest)
    allsummary.append(mylist[cold.index(min(coldest))][0])
    b = 0
    warmest = []
    while b < (len(mylist) - 1):
        warmest.append(mylist[b][5])
        b = b + 1
    i = (max(warmest))
    # print(mylist[3])
    warm = list(warmest)
    allsummary.append(mylist[warm.index(max(warmest))][0])

    windest = []
    b = 0
    while b < (len(mylist) - 1):
        windest.append(mylist[b][6])
        b = b + 1
    i = (max(windest))
    # print(mylist[3])
    wind = list(windest)
    allsummary.append(mylist[wind.index(max(windest))][0])

    m2 = gfg.Element("summary", mean_temp=allsummary[0], mean_wind_speed=allsummary[1],
                     coldest_place=allsummary[2],
                     warmest_place=allsummary[3],
                     windiest_place=allsummary[4])
    root.append(m2)
    m1 = gfg.Element("cities")
    root.append(m1)

    for i in mylist:
        b1 = gfg.SubElement(m1, i[0], mean_temp=i[1], mean_wind_speed=i[2], min_temp=i[3], min_wind_speed=i[4],
                            max_temp=i[5],
                            max_wind_speed=i[6])

    tree = gfg.ElementTree(root)

    with open(fileName, "wb") as files:
        tree.write(files)


def main():
    mylist = []
    for i in os.scandir("../parsing_serialization_task/source_data"):
        path = "../parsing_serialization_task/source_data/" + i.name
        path = path + "/2021_09_25.json"
        name = i.name
        name = name.replace(" ", "-")
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

    GenerateXML("result.xml", mylist)


def summarycity(list) -> Dict:
    result = []
    result.append(f'{(sum(list) / len(list)):.2f}')
    return result


if __name__ == "__main__":
    main()
