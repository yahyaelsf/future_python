users=[
    {
        "account_number" : "1234",
        "password" : "1234",
        "balance" : 250
    },
    {
        "account_number" : "4321",
        "password" : "4321",
        "balance" : 250
    }
]
text = """
1- show balance
2- withdrow many
3- deposit many
4- exit
"""

account = input("Enter Your account :")
is_login = False
user_index = 0
for item in users :
    if item["account_number"] == account :
        user_index = users.index(item)
        print("Login Successfully")
        is_login = True
while is_login:
    print(text)
    opertation = input("Enter Your operation :")
    match opertation :
        case "1" :
           print(f"your balance is {users[user_index]["balance"]}") 
        case "2" :
            in_withdrow = float(input("Enter your withdrow balance :"))
            users[user_index]["balance"] = users[user_index]["balance"] -in_withdrow
        case "3" :
            in_deposit = float(input("Enter your deposit balance :"))
            users[user_index]["balance"] = users[user_index]["balance"] + in_deposit
        case "4" :
            break
   