from prettytable import PrettyTable
output = {"Code": [], "Name": [], "Country": [], "Employees": [], "CEO": [], "Age": []}
out = []
output["Code"].append("liststock[b]")
output["Name"].append("listname[b]")

out.append(output.copy())
output = {"Code": [], "Name": [], "Country": [], "Employees": [], "CEO": [], "Age": []}
output["Code"].append("liststock[b]")
output["Name"].append("listname[b]")
out.append(output.copy())
newout = out

    #print('{:<10s}{:>4s}'.format(" | ".join(i['Address'])),(", ".join(i['Name'])))))

t = PrettyTable(['Name', 'Code', 'Country', 'Employees', 'CEO', 'Age'])
for i in newout:
    t.add_row([i['Name'], i['Code'], i['Country'], i['Employees'], i['CEO'], i['Age']])
print(t)