#num1 = input("Enter your first fav movie:")
#num2 = input("Enter your second fav movie:")
#num3 = input("Enter your third fav movie:")
#num = [num1, num2, num3]
#print(num)

#list1 = ["m","a","a","p"]

#copy_list1 = list1.copy()
#copy_list1.reverse()

#if(copy_list1 == list1):
#    print("palindrome")
#else:
#   print("not palindrome")

#grade = ["C", "D", "A", "A", "B", "B", "A"]
#grade.sort()
#print(grade) 

#info = {
#    "key" : "value",
 #   "name" : "Jash",
  #  "subjects" : {
   #     "python" : 99,
    #    "C" : 2, 
      #  "java" : 5
      #     
 #  "learning" : "python",\n
  #  "age" : 17,\n
   # "is_adult" : True,\n
    #44 : 52\n
#}    
#print(info["name"])
#print(info["subjects"]["python"])
#print(info["topics"])
#print(info["age"])
#print(info[44])
#info["surname"] = "Bhagat"
#print(info["surname"])

#null_dict = {}
#null_dict["name"] = "Jignesh"
#print(null_dict)

#marks = {}
#x = int(input("enter phy:"))
#marks.update({"phy" : x })

#x = int(input("enter chem:"))
#marks.update({"chem" : x })

#x = int(input("enter math:"))
#marks.update({"math" : x })
#print(marks)

#i = 1
#while i <= 100 :
#    print(i)
#    i+=1

#i = 100
#while i >= 1:
#    print(i)
#    i-=1

#i = 1
#n = int(input("enter number:"))
#while i <= 10 :
#    print((n), ("x"), (i), ("="), (n*i))
#    i+=1

#nums =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#idx = 0
#while idx < len(nums):
#    print(nums[idx])
#    idx += 1

#nums =  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#x = int(input("enter nums:"))
#i = 0
#while i < len(nums):
#    if(nums[i] == x):
#        print("Found at idx", i)
#    else:print("finding...")
#    i += 1

#i = 1
#while i<= 5:
#    print(i)
#    if(i==3):
#        break
#    i+=1
#print("End of loop")

#i=0
#while i <= 10:
#    if(i%2 !=0):
#        i+=1
#        continue
#    print(i)
#    i+=1

#nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
#x = 49
#idx = 0
#for el in nums:
#    if(el == x):
#        print("number found at idx", idx)
#    idx 

#n = int(input("enter number:"))

#for i in range(1, 11):
#    print(n*i) # any number tables
 
#for i in range(5):
#    pass
#print(6)

#if i > 5:
#    pass 
#print(3)

#n = 3
#fact = 1 
#i = 1
#while i <= n: Factorial of n number with while loop
#   fact *= i
#    i += 1

#print("factorial=", fact)

#n = 5
#fact = 1

#for i in range(1, n+1): Factorial of n number with for loop
#    fact *= i

#print("factorial=", fact)

#Functions:
#def func_name(parameter1, parameter2):
  #some work
#  return parameter1, parameter2

#func_name("argument1", "argument2") #function call

#Example;
#def calc_sum(a, b):
#    sum = a + b     #OR       return a + b 
#    print(sum)             sum = calc_sum(1, 2)
#                           print(sum)
#calc_sum(1, 2)
#calc_sum(6, 6)
#calc_sum(3, 4)
  
#def print_hello(null parameter):    
#    print("hello world")
#print_hello()
#print_hello()
#print_hello()

#average of 3 numbers

#def calc_avg(a, b, c):
#    sum = a  + b + c
#    avg = sum/ 3
#    print(avg)
#    return avg
#calc_avg(98, 97, 95)

#cities = ["Delhi", "Gurgaon", "Noida", "Pune", "Mumbai", "Chennai"]
#car = ("toyota", "suzuki", "wolkswages")
#def print_len(list):
#    print(len(list))

#print_len(cities)
#print_len(car)

#n=5
#def cal_fact(n):
#    fact = 1
#    for i in range(1, n+1):
#        fact *= i
#    print(fact)

#cal_fact(5)

#def converter(usd_val):
#    inr_val = usd_val * 83
#    print(usd_val, "USD =", inr_val, "INR")

#converter(100)

#HOMEWORK
#def number(num):
#    
#    if num % 2 == 0:
#      print("Even num")
#    else :
#      print("Odd num")
#    return num
#number(int(input("enter number=")))

#Recursive function
#def show(n):
#    if(n == 0):
#      return
#    print(n)
#    show(n-1) 
#show(3)

#def fact(n):
#    if(n == 0 or n == 1 ):
#       return 1
#    return fact(n-1)*n

#print(fact(7))

#def cal_sum(n):
#    if(n ==0):
#        return 0
#    return cal_sum(n-1) + n
#sum = cal_sum(10)    
#print(sum)
