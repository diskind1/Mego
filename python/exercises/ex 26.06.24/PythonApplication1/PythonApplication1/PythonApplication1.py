# x=4
# s=0
# for i in range(x):
#     print(x)
#     if(s<6):
#         x+=10
#     s=s+1
   



# #   werxy     a;slkjfnwwwwerxtttrlsfhsf
# #   aaa     a;slkjfnaawaerlsfhsf

# def SubString(s1, s2):
#     i1=0
#     i2=0
#     while(i1<len(s1)):
#         while(i2<len(s2)):
#             if((s1[i1])<(s2[i2])):
#                 return False
#             if(s1[i1]==s2[i2]):
#                 i2+=1
#                 break
#             i2+=1
#         if(i2==len(s2)):
#             return False
#         i1+=1
#     return True            
# print(SubString("afkpw", "abcdefghijklmnop"))







# def T(rows):
#     space=rows-1
#     stars=1
#     for r in range(rows):
#         for k in range(space):
#             print(end=" ")
#         space-=1
#         for k in range(stars):
#             print(end="*")
#         stars+=2
#         print()
# T(8)        
# '''            
#     *
#    ***
#   *****
#  *******
# *********
 
# '''








# def D(x):
#     sum=0
#     for i in range(1, x):
#         if(i%2==1):
#             print(i, end=" - ")
#             sum+=i
#         else:
#             print(i, end=" + ")
#             sum-=i
#     print(x, end = " = ")
#     if(x%2==1):
#         sum+=x
#     else:
#         sum-=x
#     print(sum)
       
# D(8)            
# #   1-2+3-4+5-6+7=???







# def G(x):
#     sum=0
#     i=1
#     while(i<x):
#         print(i, end=" + ")
#         sum+=i
#         i+=1
#     print(i, " = ", sum+i)

# G(8)





# def G(x):
#     sum=0
#     for i in range(1, x):
#         print(i, end=" + ")
#         sum+=i
#     print(x, " = ", sum+x)

# G(8)








# def Show(a):
#     # for r in range(len(a)):  
#     #     print(a[r])
#     for r in range(len(a)):  
#         for c in range(len(a[r])):
#             print(a[r][c], end=" - ")
#         print()
           
# a=[
#     [3,6,5,4],
#     [9,8,7,6],
#     [1,2,3,4],
#     [5,5,6,6],
#     [1,2,2,7],
# ]
# Show(a)







# def Rec(x):
#     if(x>9):
#         return x%10 + Rec(x//10)
#     return x
# print(Rec(12345))







# def A(x):
#     sum=0
#     while(x>9):
#         sum+=x%10
#         x=x//10
#     return sum+x


# r=A(12345)
# print(r)
# print(A(75756))






# a=[44.55, 44, "sdgdg", '$', True]
# print(a)
# a.append(55555)
# print(a)






# a=[4234,6756,342,65]
# for i in range(len(a)):
#     v=a[i]
#     sum=0
#     while(v>0):
#         sum+=v%10
#         v=v//10
#     print(sum)
# a.append(7777)    
# print(a)

   






# for x in range(9, 2, -1):
#     print(x, end=" ")
# print()






# x=9
# while(x>2):
#     print(x, end=" ")
#     x-=1
# print()

            









# def T(rows):
#     spaces = rows - 1
#     stars =1
#     for r in range(rows):
#         for k in range(spaces):
#             print(end =" ")
#         spaces-=1
#         for k in range(stars):
#             print(end="*")
#         stars+=2
#         print()
# T (int(input("Enter a number: ")))










# def G(x):
#     sum=0
#     i=1
#     while (i<x):
#         print (i, end=" + ")
#         sum+=i
#         i+=1
#     print (i, " = ", sum+i)
# G(8)



# def aa(): 
#     a =  input("Enter a number: ")
#     sum=0
#     while (a>0):
#         sum=a+a
#     print (sum)
# aa()






# def REC(x):
#     if (x>9):
#         return x%10 + REC(x//10)
#     return x
# print (REC(123455))








# def A(x):
#     sum=0
#     while(x>9):
#         sum+=x%10
#         x=x//10
#     return sum+x

# r=A(123455)
# print(r)
# print(A(123455))








# a=[5645,5464,46,546]
# for i in range(len(a)):
#    v=a[i]
#    sum=0
#    while(v>0):
#       sum+=v%10
#       v=v//10
#    print(sum)
# a.append(7777)
# print(a)