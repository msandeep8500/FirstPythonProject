def computeaverage(number_list):
    return sum(number_list)/len(number_list)

number_list =[]
for i in range(5):
      number= int(input("Please enter number"))
      number_list.append(number)
      i += 1

print(number_list)

print(computeaverage(number_list))