




















# def longest_unique_substring(s):
#     max_substring = ""
#     current_substring = ""
#     unique_chars = set()

#     for char in s:
#         if char in unique_chars:
#             while current_substring[0] != char:
#                 unique_chars.remove(current_substring[0])
#                 current_substring = current_substring[1:]
#             current_substring = current_substring[1:] + char
#         else:
#             unique_chars.add(char)
#             current_substring += char

#         if len(current_substring) > len(max_substring):
#             max_substring = current_substring

#     return [max_substring, s.index(max_substring)]

# # דוגמה לשימוש בפונקציה
# input_string = "abcabbcb"
# output_substring = longest_unique_substring(input_string)
# print(output_substring)  # ידפיס: ["bb", 4]
# # לא נכון!!!!!!

















# def longest_unique_substring(s):
#     max_substring = ""
#     current_substring = ""
#     unique_chars = set()

#     for char in s:
#         if char in unique_chars:
#             while current_substring[0] != char:
#                 unique_chars.remove(current_substring[0])
#                 current_substring = current_substring[1:]
#             current_substring = current_substring[1:] + char
#         else:
#             unique_chars.add(char)
#             current_substring += char

#         if len(current_substring) > len(max_substring):
#             max_substring = current_substring

#     return max_substring

# # דוגמה לשימוש בפונקציה
# input_string = "abcabbcb"
# output_substring = longest_unique_substring(input_string)
# print(output_substring)  # ידפיס: "bb"
# # לא נכון!!!!!!!









# def most_frequent_char(s):
#     char_count = {}
    
#     # ספירת התווים
#     for char in s:
#         char_count[char] = char_count.get(char, 0) + 1
    
#     # מציאת התו הנפוץ ביותר
#     max_count = max(char_count.values())
#     most_frequent_chars = [char for char, count in char_count.items() if count == max_count]
    
#     return most_frequent_chars

# # דוגמה לשימוש בפונקציה
# input_string = "dont worry"
# output_chars = most_frequent_char(input_string)
# print(output_chars)  # ידפיס: ['o', 'r']








# def filter_even_numbers(numbers):
#     return [num for num in numbers if num % 2 == 0]

# # דוגמה לשימוש בפונקציה
# input_list = [6, 4, 7, 3, 2, 1]
# output_list = filter_even_numbers(input_list)
# print(output_list)  # ידפיס: [6, 4, 2]










# def build_string(*numbers):
#     return " ".join(map(str, numbers))

# # דוגמה לשימוש בפונקציה
# result = build_string(1, 2, 3, 4, 5)
# print(result)  # ידפיס: "1 2 3 4 5"






# first_name = input("Enter a First Name: ")
# last_name = input("Enter a Last Name: ")
# your_namber = input("Enter your number: ")
# print (first_name, last_name)
# print (your_namber)








# def product_calculate(a=1, b=1, c=input("Enter a number: ")):
#     product = a * b * c
#     print(f"The product is: {product}")
#     return product

# print(product_calculate(2,1,1))






# # def string_manipulate(s):
# #     # הדפסת האורך הכולל של המחרוזת
# #     print(f"Total length of the string: {len(s)}")
    
# #     # החזרת המחרוזת באותיות גדולות
# #     upper_case = s.upper()
# #     print(f"Uppercase: {upper_case}")
    
# #     # החזרת המחרוזת באותיות קטנות
# #     lower_case = s.lower()
# #     print(f"Lowercase: {lower_case}")
    
# #     # החזרת המחרוזת בהיפוך
# #     reversed_string = s[::-1]
# #     print(f"Reversed: {reversed_string}")

# # # דוגמה לשימוש בפונקציה
# # string_manipulate("MenMI")






# def string_manipulate (s):
#     print (f"Uppercase: {s.upper()}")
#     print (f"Lowercase: {s.lower()}")
#     print (f"Reversed: {s[::-1]}")
#     print (f"Total length of the string: {len(s)}")
# string_manipulate(input("Enter a word: "))






# def details_print (name, age=18):
#     print(f"name: {name}, age: {age}")
#     if age > 18:
#         print ("adult")
#     else:
#         print ("Minor")
        
# details_print("menni",22)
    









# def analysis_text(text):
#     # a. ספירת מילים
#     words = text.split()
#     num_words = len(words)
    
#     # b. מציאת המילה הארוכה ביותר
#     longest_word = max(words, key=len)
    
#     # c. ספירת תווים ספציפיים
#     specific_chars = ['a', 'e', 'i', 'o', 'u']
#     char_count = {char: text.count(char) for char in specific_chars if text.count(char) < 5}
    
#     # d. ספירת וחיבור מספרים
#     numbers = [int(num) for num in text.split() if num.isdigit()]
#     sum_numbers = sum(numbers) if len(numbers) > 10 else None
    
#     # הדפסת המידע
#     print(f"Number of words: {num_words}")
#     print(f"Longest word: {longest_word}")
    
#     if char_count:
#         print("Specific character counts:")
#         for char, count in char_count.items():
#             print(f"{char}: {count}")
    
#     if sum_numbers is not None:
#         print(f"Sum of numbers: {sum_numbers}")

# # דוגמה לשימוש בפונקציה
# analysis_text("This is an example string with some numbers 12345 and some specific characters")




    







# def check_characters(string1,string2,string3):
#     if ',' in string1:
#         a=string1.count(",")
#         print (f"I've found {a} commas in your string!")
#     if '.' in string1: 
#         b=string2.count(".")
#         print (f"I've found {b} periods in your string!")
#     if '!' in string1:   
#         c=string3.count("!")
#         print (f"I've found {c} '!' in your string!")
        
# check_characters("hello world!- .","hd","mego!!!")








# def check_characters(string1):
#     if ',' in string1:
#         print (f"I've found a commas in your string!")
#     if '.' in string1:      
#         print (f"I've found a periods in your string!")
#     if '!' in string1:     
#         print (f"I've found a '!' in your string!")
        
# check_characters("hello world!- .")



# def calculate_product(c, a=1, b=1):
#     print (a*b*c)
#     return(a*b*c)

# calculate_product(int (input("Enter your choice: ")))





# input_string = input("Enter a string: ")






# a = input("Enter a word: ")
# b = a.lower()
# c = a.upper()
# d = a[::-1]
# print (b,c,d)





# a = input("Enter a word: ")
# b = input("Enter a word: ")
# c = input("Enter a word: ")
# print (a +",",b +",",c)



# first_string = input("Enter a First Name: ")
# last_string = input("Enter a Last Name: ")
# print (f"Your name is: {first_string} {last_string}")














# # קלט מהמשתמש
# fruit_name = input("Enter name of fruit: ")
# number = int(input("Enter a number: "))

# # בדיקה לפי שם הפרי והמספר
# if fruit_name == "apple":
#     if number > 5:
#         print("Lots of apples!")
#     else:
#         print("A few apples.")
# elif fruit_name == "banana":
#     if number % 2 == 0:
#         print("Even bananas!")
#     else:
#         print("Odd bananas!")
# else:
#     print("Other fruit.")

















# # קלט מהמשתמש
# input_number = int(input("Enter a number: "))
# input_string = input("Enter a string: ")

# # בדיקה אם המספר זוגי
# if input_number % 2 == 0:
#     if 'e' in input_string:
#         print("Even and has an 'e'")
#     else:
#         print("Even but no 'e'")
# # אחרת, המספר אי-זוגי
# else:
#     print(f"The last character in the string is '{input_string[-1]}'")














# input_string = input("Enter a string: ")
# if len(input_string) > 10 and '@' in input_string:
#     print ("high")
# elif len(input_string) >5<10 and '!' in input_string:
#     print("Medium")
# else: print ("Low")
    










# # קלט מהמשתמש
# input_string = input("Enter a string: ")

# # בדיקה אם המחרוזת מכילה את המילה "hello"
# if "hello" in input_string:
#     print("Hello to you too!")
# # בדיקה אם יש יותר משלושה פסיקים במחרוזת
# elif input_string.count(',') > 3:
#     print("That's a lot of commas.")
# # אחרת, הדפס את מספר התווים במחרוזת
# else:
#     print(f"The string has {len(input_string)} characters.")












# # קלט מהמשתמש
# input_string = input("Enter a string: ")
# input_number = int(input("Enter a number: "))


# a=input_string[:input_number]

# # בדיקה והדפסה לפי התנאים
# if input_number > len(input_string):
#     a=input_string.upper
# print(a)

# # #עוד אפשרות

# # # קלט מהמשתמש
# # input_string = input("אנא הכנס מחרוזת: ")
# # input_number = int(input("אנא הכנס מספר: "))

# # # בדיקה והדפסה לפי התנאים
# # if input_number > len(input_string):
# #     print(input_string.upper())
# # else:
# #     print(input_string[:input_number])
















# a=input("Enter a long srting: ")
# b=input("Enter a short srting: ")











# a=input("Enter a few words: ")

# words = a.split()
# num_words = len(words)
# num_commas = a.count(',')
# num_periods = a.count('.')

# print ("number of words", num_words)
# print ("number of commas", num_commas)
# print ("number of periods", num_periods)









# a=input("Enter a word: ")
# b=a[2:5]
# print (b)










# a=input("Enter a word: ")
# if a[0]== a[-1]:
#     print ("Yes")
# else:
#     print ("No")
#     #בודק אם האות הראשונה והאחרונה שבקלט - זהות


#עוד אפשרות
# a=input("Enter a word: ")
# if a[0]== a[len(a) -1]:
#     print ("Yes")
# else:
#     print ("No")





    



# a=input ("enter a word: ")
# lower=a.lower() #הופך הכל לאותיות קטנות
# upper=a.upper() #הופך הכל לאותיות גדולות
# revers=a[::-1] #הופך את המחרוזת מהסוף להתחלה
# print (lower,upper,revers)










# a=input ("enter a word: ")
# b=input ("enter a word: ")
# c=input ("enter a word: ")
# print (a+",",b+",",c)










# a="menni"
# b="jerusalem"
# print(a,b)
