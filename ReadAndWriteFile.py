from mycomputation2 import Sort_Cities
cities_list =[]
with open("Cities","r") as f:
    for lines in f:
        cities_list.append(lines.rstrip("\n"))

print(Sort_Cities(cities_list))
with open("SortedCities","w") as f:
    f.write(str(Sort_Cities(cities_list)))