import json
import xml.etree.ElementTree as gfg


json1_file = open('2021_09_25.json')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)

# print(json1_data['current'])
# print(json1_data['hourly']['temp'])
all_temp = []
for i in json1_data['hourly']:
    all_temp.append(i['temp'])
print(f'{sum(all_temp) / len(all_temp):.2f}')
print(f'{max(all_temp):.2f}')
print(f'{min(all_temp):.2f}')
all_wind = []
for i in json1_data['hourly']:
    all_wind.append(i['wind_speed'])
print(f'{sum(all_wind) / len(all_wind):.2f}')
print(f'{max(all_wind):.2f}')
print(f'{min(all_wind):.2f}')


def GenerateXML(fileName):
    root = gfg.Element("Catalog")
    m1 = gfg.Element("cities")
    root.append(m1)

    b1 = gfg.SubElement(m1, "Barcelona")
    b1.text = f'{sum(all_temp) / len(all_temp):.2f}'

    tree = gfg.ElementTree(root)

    with open(fileName, "wb") as files:
        tree.write(files)

if __name__ == "__main__":
    GenerateXML("Catalog.xml")