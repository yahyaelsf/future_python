# name = "yahya el saftawi"
# print(name.title())
# email = "yahya@gmail.com"
# print(email.replace(".com" , ".net"))
# text = "welcome student in python cource"
# title_text = text.title()
# split_text = title_text.split()
# result = "-".join(split_text)
# text_list = text.replace(" " , "-")
# print(split_text)
# print(result)
# print(email.strip("*"))
# password = "yahya el@saftawi.com"
# print(password.endswith("wi"))
# print(password.find("@"))
# email = input("enter your email :")
# indx1 = email.find("@")
# username = email[0:indx1]
# indx2 = email.find(".")
# company = email[indx1+1:indx2]
# print(f"the user name is {username}")
# print(f"the company name is {company}")
# print(f"the extintion is {email[indx2+1:]}")

# email = input("enter your email :")
# fisrt_split = email.split("@")
# username = fisrt_split[0]
# second_split = fisrt_split[1].split(".")
# print(f"the user name is {username}")
# print(f"the company name is {second_split[0]}")
# print(f"the extintion is {second_split[1]}")


# """
# 1- 0 endxing (oedered)
# 2- mutable (add , edit , delete)
# 3- not uniqe element 
# crud application : c => create , r => read , u => update , delete
# """

# names.insert(2 ,"samar")
# print(names)
# names.remove("yahya")
# names.pop(0)
# names[1] = "yahya"
# names.reverse()
# print(names.index("yahya"))
# names = ["saja" , "yahya" , "mohammed" , "zyad" ,"yahya"]
# value1 = input("enter update name :")
# new_value = input("Enter enw value")
# indx = names.index(value1)
# names[indx] = new_value
# print(names)
# cureceis = ["usd" , "eur" , "job" , "tls"]
# valuse = [3.2 , 3.5 , 4.5 , 1.0]

# cur = input("enter your caeuncy :")
# amount = float(input("enter your amount :"))

# indx = cureceis.index(cur)
# result = valuse[indx] * amount
# print(f"the total amount is {result} from {cur}")
# inventory = {
#     "laptop": {"price": 800, "stock": 10},
#     "mouse": {"price": 20, "stock": 50},
#     "keyboard": {"price": 45, "stock": 30}
# }
# print(inventory["laptop"]["price"])