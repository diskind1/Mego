class Tank:
    def __init__(self, capacity, amount=0):
        self.__capacity=capacity
        self.amount=amount
    def SetCapacity(self, capacity):
        self.__capacity=capacity
    def GetCapacity(self):
        return self.__capacity
    def amounttf(self, amount):
        if(self.amount>0):
         return True
        return False   
        
        



    ###   main   ###
    
y=Tank (15)
Tank.amounttf(y)
 



# show(Tank)

















# from operator import indexOf
# import random
# class Talmid:
#     def __init__(self, name, grades):
#         self.__name=name
#         self.__grades=grades
#         self.__ave=0
#         for i in range(len(grades)):
#             self.__ave+=grades[i]
#         self.__ave=self.__ave/len(grades)
#     def SetName(self, name):
#         self.__name=name
#     def SetGrades(self, grades):
#         self.__grades=grades
#         self.__ave=0
#         for i in range(len(grades)):
#             self.__ave+=grades[i]
#         self.__ave=self.__ave/len(grades)
#     def GetName(self):
#         return self.__name
#     def GetGrades(self):
#         return self.__grades
#     def GetAve(self):
#         return self.__ave
   
# ####    MAIN    ####
# def Show(k):
#     for i in range(len(k)):
#         print(k[i].GetName(),k[i].GetAve(), k[i].GetGrades())
   
# def GetBest(k):
#     best=0
#     indexOfBest=0
#     for i in range(len(k)):
#         if(best<k[i].GetAve()):
#             best=k[i].GetAve()
#             indexOfBest=1
#     return indexOfBest


# kita=[None]*44
# names=["Reuven", "Shimon", "Levi", "Yehuda"]
# for i in range(len(kita)):
#     n=names[random.randint(0, len(names)-1)]
#     g=[0]*6
#     for k in range(len(g)):
#         g[k]=random.randint(0,100)
#     kita[i]=Talmid(n, g)

# Show(kita)
# i=GetBest(kita)
# print()
# print()
# print()
# print(kita[i].GetName(),kita[i].GetAve(), kita[i].GetGrades())
# print()
# print()
# print()
# # print(kita[i].Tostring())


# # class Talmid:
# #     def __init__(self, name, grades):
# #         self.__name=name
# #         self.__grades=grades
# #         self.__ave=0
# #         for i in range(len(grades)):
# #             self.__ave+=grades[i]
# #         self.__ave=self.__ave/len(grades)
# #     def SetName(self, name):
# #         self.__name=name
# #     def SetGrades(self, grades):
# #         self.__grades=grades
# #         self.__ave=0
# #         for i in range(len(grades)):
# #             self.__ave+=grades[i]
# #         self.__ave=self.__ave/len(grades)
# #     def GetName(self):
# #         return self.__name
# #     def GetGrades(self):
# #         return self.__grades
# #     def GetAve(self):
# #         return self.__ave
   
# # ####    MAIN    ####
# # t1=Talmid("eee", [33,55,44,66,99])  #  
# # print(t1)
# # kita=[]
# # kita.append(t1)
# # t1=Talmid("YYYY", [44,66,54,99])
# # print("t1", t1)
# # kita.append(t1)
# # print(kita[0])
# # print(kita[1])
# # print(kita)
# # print()





# # class Talmid:
# #     def __init__(self, name, grades):
# #         self.__name=name
# #         self.__grades=grades
# #         self.__ave=0
# #         for i in range(len(grades)):
# #             self.__ave+=grades[i]
# #         self.__ave=self.__ave/len(grades)
# #     def SetName(self, name):
# #         self.__name=name
# #     def SetGrades(self, grades):
# #         self.__grades=grades
# #         self.__ave=0
# #         for i in range(len(grades)):
# #             self.__ave+=grades[i]
# #         self.__ave=self.__ave/len(grades)
# #     def GetName(self):
# #         return self.__name
# #     def GetGrades(self):
# #         return self.__grades
# #     def GetAve(self):
# #         return self.__ave
   
# # ####    MAIN    ####    

# # t1=Talmid("eee", [33,55,44,66,99])
# # print(t1.GetAve(), t1.GetName(), t1.GetGrades())
# # g=t1.GetGrades()
# # g.append(77)
# # t1.SetGrades(g)
# # print(t1.GetAve(), t1.GetName(), t1.GetGrades())









