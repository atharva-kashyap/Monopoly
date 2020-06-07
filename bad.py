list = []
dict1 = {"Rahul":"Vaidehi", "Rachel":"Ross", "Monica":"Chandler", "Debra":"Ray"}
dict2 = {"Marie":"Frank", "Phoebe":"Mike", "Kampana":"Sam", "Kriti":"Sri"}
dict3 = {"Sami":"Ryan", "Maddie":"Josh", "Abby":"Addie", "Anshita":"Mohammed"}
list.append(dict1)
list.append(dict2)
list.append(dict3)
print(list)

for i in list:
    print(i)
    for k,v in i.items():
        print(i[k])