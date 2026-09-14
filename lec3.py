# user = {
#     "id" : "404024234",
#     "name" : "yahya",
#     "age" : 26, 
#     "is_dtudent" : False,
#     "grades" : {
#         "math" : 90,
#         "arabic" : 70,
#         "seience" : 80
#     }
# }
# print(user["grades"]["math"])
# user["grades"]["english"] = 98
# print(user["grades"])
# user["grades"].update({"sport" : "50"})
# user.pop("age")
# print(user)
# print(user.items())
# input_cur = input("Enter Your currencu (usd , eur , jod , tls) :").lower().strip()
# amount = float(input("Enter Your amount :"))
# curency = {
#     "usd" : 3.2,
#     "eur" :3.5,
#     "jod" : 4.5,
#     "tls": 1.0
# }
# result = curency[input_cur] * amount
# print(f"the total amount is {result} from {input_cur}")
# store = {
#     "labtop" : {
#         "quantity" : 100,
#         "price" : 1230
#     },
#     "mobile" : {
#         "quantity" : 230,
#         "price" : 720
#     }
# }
# total_labtop = store["labtop"]["quantity"] * store["labtop"]["price"]
# total_mobile = store["mobile"]["quantity"] * store["mobile"]["price"]
# result = f"""
# total money in labtop is {total_labtop}$,
# total money in mobile is {total_mobile}$,
# """
# print(result)

# tuple1 = (1 , 2 ,3 ,10 ,15 ,1 )
# print(tuple1[0 : 4])
# set1 = { 5 , 4 ,10 , 2 , 4}
# print(set1)
# list1 = [1 , 1, 2, 2, 3, 3]
# newlist = set(list1)
# print(newlist)
# set1 = {1,2,3}
# set2 = {3,4,5}
# print(5 in set1)
# if condition :
#  
# age = 19
# if age == 18 :
#     print("you are strong")
# elif age < 20  :
#     print("you are still Young")
# elif age > 50 :
#     print("you are old man")
# else :
#     print("you are youth")
# email = False 
# password = False 
# if email and password :
#     print("Login succeefully ")
# elif not email and not password :
#     print("Error in email & password ")
# elif not email :
#     print("Error in email ")
# elif not password :
#     print("Error in password ")


admins = ["ahmad" , "yahya" , "ali" ,"samar"]
print(admins)
print("1- add to list")
print("2- edit from list")
oper = input("enter Your operation :")
if oper == "1" :
    new_user = input("Enter new user :")
    admins.append(new_user)
    print("admins add successfully")
elif oper == "2":
    name = input("Enter admin name :")
    if name in admins :
        edit_amdin = input("Enter new value for your admin")
        index = admins.index(name)
        admins[index] = edit_amdin
        print("admin edit successfully ")
    else :
        print("error not found")
else:
    print("Error")

