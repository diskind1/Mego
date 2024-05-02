





# n1=int(input("Enter first number : "))
# n2=int(input("Enter second number : "))
# c=0
# s=0
# e=0
# while(n1*(-1)!=n2):
#    c+=2
#    if(n1>0):
#       s+=n1
#    if(n2>0):
#       s+=n2
#    if(n1==n2):
#       e+=1
#    n1=int(input("Enter first number : "))
#    n2=int(input("Enter second number : "))
# print(c, s, e)




# def IsPeak(arr, index):
#     if(index==0 or index==len(arr)-1):
#         return False
#     if(arr[index-1]<arr[index] and arr[index+1]<arr[index]):
#         return True
#     return False
# a=[1,2,3,4,5,5,6,4,5,6,2,3,3,2,1,2,1,3,4,2,3,1]
# c=0
# for i in range(1, len(a)-1):
#     if(IsPeak(a, i)==True):
#         c+=1
# print(c)

# s=input("Enter a string : ")
# c=0
# while(s[0]!='Z' and s[len(s)-1]!='Z'):
#     if(s[0]=='X' and s[len(s)-1]=='X'):
#         c+=1
#     s=input("Enter a string : ")
# print(c)



# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         c=-11
#         t=[0]*len(l)
#         for a in range(len(l)):
#             if(t[a]==0):
#                 c=1
#                 t[a]=1
#                 for b in range(a+1, len(l)):
#                     if(l[a]==l[b]):
#                         c+=1
#                         t[b]=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))



# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)
           




# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)













# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:  
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")





# s=input("Enter a string : ")
# c=0
# while(s[0]!='Z' and s[len(s)-1]!='Z'):
#     if(s[0]=='X' and s[len(s)-1]=='X'):
#         c+=1
#     s=input("Enter a string : ")
# print(c)


# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         c=-11
#         t=[0]*len(l)
#         for a in range(len(l)):
#             if(t[a]==0):
#                 c=1
#                 t[a]=1
#                 for b in range(a+1, len(l)):
#                     if(l[a]==l[b]):
#                         c+=1
#                         t[b]=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))




# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)
           




# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)













# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:  
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")









# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         c=-11
#         t=[0]*len(l)
#         for a in range(len(l)):
#             if(t[a]==0):
#                 c=1
#                 t[a]=1
#                 for b in range(a+1, len(l)):
#                     if(l[a]==l[b]):
#                         c+=1
#                         t[b]=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# print(A(l))



# def A(l):
#     if(len(l)%2==1):
#         return False
#     else:
#         for a in range(len(l)):
#             c=0
#             for b in range(len(l)):
#                 if(l[a]==l[b]):
#                     c+=1
#             if(c!=2):
#                 return False
#         return True
# l=[1, 3, 4, 2, 5, 2, 1, 3, 5, 4, 6, 6]
# t=[1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0]
# A(l)
           




# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i==len(s)-1):
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            m+=1
# print(m)













# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:  
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")
#     else:
#        print("NO")





# m=0
# for i in range(3):
#     s=input("Enter a string : ")
#     i=0
#     c=0
#     while(i<len(s)-1):
#        if(s[i]=='A'):
#           if(s[i+1]=='A'):
#              break
#           c+=1
#        i+=1
#     if(i<len(s)-1):
#        print("NO")
#     else:  
#         if(s[i]=='A'):
#            c+=1
#         if(c>1):
#            print("YES")
#         else:
#            print("NO")
# print(m)



# s=input("Enter a string : ")
# i=0
# c=0
# while(i<len(s)-1):
#    if(s[i]=='A'):
#       if(s[i+1]=='A'):
#          break
#       c+=1
#    i+=1
# if(i<len(s)-1):
#    print("NO")
# else:  
#     if(s[i]=='A'):
#        c+=1
#     if(c>1):
#        print("YES")









# # # מחרוזת נקראת "מחרוזת תקינה" אם המחרוזת כוללת לפחות שתי אותיות 'A 'אבל לא כוללת רצף "AA".
# # # כתבו קטע ת וכנית הקולטת 23 מחרוזות. הקטע יחשב וידפיס את מספר ה"מחרוזות התקינות".
# # # לדוגמה:
# # # המחרוזת ABBA כוללת שתי אותיות 'A 'ולא כוללת את הרצף "AA "
# # ולכן מקיימת את התנאי למחרוזת תקינה

# def is_valid_string(s):
#     return s.count('A') >= 2 and 'AA' not in s

# # קליטת 23 מחרוזות ובדיקת תקינותן
# valid_strings_count = 0
# for _ in range(23):
#     user_string = input("Please enter a string: ")
#     if is_valid_string(user_string):
#         valid_strings_count += 1

# # הדפסת מספר המחרוזות התקינות
# print(f"The number of valid strings is: {valid_strings_count}")























# # # כתבו קטע תוכנית הקולטת מספרים שלמים עד שייקלט המספר .500 קטע תוכנית צריך:
# # # - להדפיס עבור כל מספר אי-זוגי את סכום ספ רותיו.
# # # - לחשב ולהדפיס את ממוצע של המספרים שנקלטו.

# # קליטת מספרים שלמים עד שייקלט המספר 500
# numbers = []
# while True:
#     user_input = input("Please enter a whole number (to finish type '500'): ")
#     if user_input == '500':
#         break
#     numbers.append(int(user_input))

# # הדפסת סכום ספרות המספרים האי-זוגיים
# for num in numbers:
#     if num % 2 != 0:
#         digit_sum = sum(int(digit) for digit in str(abs(num)))
#         print(f"The sum of the digits of the number {num} is {digit_sum}")

# # חישוב והדפסת ממוצע המספרים
# if len(numbers) > 0:
#     average = sum(numbers) / len(numbers)
#     print(f"The average of the numbers taken is {average:.2f}")
# else:
#     print("No numbers entered")

