




# # # מחרוזת שמייצגת "מספר נייד תקין" היא מחרוזת העונה לשלושה תנאים:
# # # • שלושת התווים ראשונים הם קידומת ) 050 , 051 , 052 , 053 , 054 , 055 , 056 , 057 , 058 .)
# # # • התו הרביעי הוא מקף )-(.
# # # • שבעת התווים הבאים הם ספרות.
# # # לדוגמה:
# # # המחרוזת 050-1230567 היא מספר נייד תקין.
# # # כתבו קטע תוכנית הקולטת מחרוזות עד שתקלט מחרוזת שהיא מספר נייד תקין. יש להדפיס מספר המחרוזות
# # # שנקלטו.

# import re

# def is_valid_mobile_number(number):
#     pattern = r'^05[0-8]-\d{7}$'
#     return bool(re.match(pattern, number))

# count = 0
# while True:
#     number = input("Enter a mobile phone number: ")
#     count += 1
    
#     if is_valid_mobile_number(number):
#         break

# print(f"The number of strings received: {count}")













# # # מספר שלם חיובי נקרא "מספר מושלם" אם הוא מתחלק בסכום ספרותיו.
# # # לדוגמה:
# # # מספר 12 הוא מספר מושלם, מספר 24 הוא מספר מושלם, מספר 25 אינו מספר מושלם.
# # # כתבו קטע ת וכנית להדפסת כל המספרים המושלמים מ - 1 עד 1,000 .


# def sum_of_digits(num):
#     return sum(int(digit) for digit in str(num))

# def is_perfect_number(num):
#     return num % sum_of_digits(num) == 0

# perfect_numbers = [num for num in range(1, 1001) if is_perfect_number(num)]

# print("The perfect numbers from 1 to 1,000 are:")
# for num in perfect_numbers:
#     print(num)



















# # # כתבו קטע קוד שקולט מספרים שלמים עד שייקלט מספר תלת ספרתי. 
# # # יש להדפיס את מספר הגדול ביותר
# # # שנקלט ואת מספר הקטן שנקלט.


# max_num = float('-inf')
# min_num = float('inf')

# while True:
#     num = int(input("Enter a whole number: "))
    
#     if num >= 100 and num <= 999:
#         print("A three-digit number was entered. End of input.")
#         break
    
#     max_num = max(max_num, num)
#     min_num = min(min_num, num)

# if max_num == float('-inf') and min_num == float('inf'):
#     print("No numbers were entered before the three-digit number.")
# else:
#     print(f"The largest number received: {max_num}")
#     print(f"The smallest number received: {min_num}")







# # # -*- coding: utf-8 -*-
# # def main():
# #     print("היי")
# # if "__name__" == "__main__":
# #     main()













# def SpecialNumber(n):
#     r=0
#     while(n>0):
#         r+=n%10
#         n//=10
#         r-=n%10
#         n//=10
#     return r==0

#   84235

# def F(a):
#     if(len(a)%3!=0):
#         return False
#     td=len(a)//3
#     i=0
#     while(i<td):
#         if(not(a[i]==a[i+td] ==a[i+td+td])):
#             return False
#         i+=1
#     return True

# #   1+4*log(x)
# def DZ(x):
#     c=0
#     while(x>0):
#         if(x%2==0):
#             c+=1
#         x//=10
#     return c
# #   1 + 1 + 5*n(log)
# def DA(a):
#     mZ=0
#     for i in range(0, len(a), 1):
#         m=DZ(a[i])
#         if(m>mZ):
#             mZ=m
#     return mZ




# def F(a):       #   0
#     if(a==0):
#         return 0
#     return 1 + F(a//10)

# def F(a):       #   2
#     if(a==0):
#         return 0
#     return 1 + F(a//10)     #   1+??    1+0=1

# def F(a):       #   23
#     if(a==0):
#         return 0
#     return 1 + F(a//10)     #   1+???   1+1=2

# def F(a):   #   234
#     if(a==0):
#         return 0
#     return 1 + F(a//10) #   1+???       1+2=3
# print(F(234))




# class Tank:
#     def __init__(self, capacity, amount=0):
#         self.__capacity=capacity
#         self.amount=amount
#     def SetCapacity(self, capacity):
#         self.__capacity=capacity
#     def GetCapacity(self):
#         return self.__capacity
#     def B(self):
#         return self.amount>0
#     def IsPossible(self, num, op):
#         if(op=='+'):
#             if(self.amount+num>self.__capacity):
#                 return False
#             self.amount+=num
#         else:
#             if(self.amount-num<0):
#                 return False
#             self.amount-=num
#         return True
# ##########################
# def Fill(t1:Tank, t2:Tank):
#     r=t2.GetCapacity()-t2.amount
#     if(t1.amount<=r):
#         return t1.amount
#     else:
#         return r
 








# name1 = input("enter your first name: ");
# name2 = input("enter your last name: ");
# age = int(input("enter your age: "));
# print (name1,name2)
# print (age)