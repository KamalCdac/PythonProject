name = input("Enter your name: ")

result1 = len(name)
print(result1)

result2 = name.find("k") # find always returns first occurrence
print(result2)

# rfind method returns -1 if there are no results
result3 = name.rfind("a") # rfind always returns last occurrence
print(result3)

result4 = name.capitalize() # first letter will be capital
print(result4)

result5 = name.upper() # All letter will be capital
print(result5)

result6 = name.lower() # All letter will be lower case
print(result6)

result7 = name.isdigit() # It only returns TRUE if string contains only number and combination with strings will return FALSE
print(result7)

result8 = name.isalpha() # It only returns TRUE if string contains only alphabets else return FALSE if there is space then also return false
print(result8)
#-------------------------------------------------->>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>----------------------->>>>>>>>>>>
phone_number = input("Enter your Phone number # : ")
result9 = phone_number.count("2")
print(result9)

result10 = phone_number.replace("-", " ")
print(result10)

#print(help(str)) # list of all string methods available
#---------------------------------------------------------------------------------------------
#    Exercise : Validate user input                                                          #
#               1. Username is no more than 12 characters                                    #
#               2. Username must not contain spaces                                          #
#               3. Username must not contain digits                                          #
#---------------------------------------------------------------------------------------------

user_name = input("Enter your user name: ")
user_name_len = len(user_name)
user_name_digits = user_name.isdigit()

if user_name_digits:
    print("Username must not contain digits")
else:
    print("Username do not contains any digits")

if not user_name.isalpha() :
    print("Username contains digits ISALPHA method")
else:
    print("Username does not contains digits ")
if not user_name.find(" ") == -1:
    print("Username must not contain spaces")
else:
    print("Username do not contains any space")
if user_name_len > 12 :
    print("Username can't be more than 12 characters")
else:
    print(f"Welcome {user_name}")

