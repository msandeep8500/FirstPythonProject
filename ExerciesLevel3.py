def maxNumberinList(numberlist):
      maxnumber=0
      for number in numberlist:
          if number > maxnumber :
              maxnumber =number
      return maxnumber



number_list = [3,4,6,7,8,50]
print(maxNumberinList(number_list))

