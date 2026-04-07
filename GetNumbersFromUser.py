def computeaverage(number_list):
    return sum(number_list)/len(number_list)


number_list =[]
ask_for_numbers = True

while ask_for_numbers:
    user_number= int(input("Enter number"))
    if user_number == 0:
        ask_for_numbers= False
    else:
        number_list.append(user_number)

print(computeaverage(number_list))



