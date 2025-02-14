def user_info(name , age , **info):
    print("Name:" , name)
    print("Age: " , age)
    for key , value in info.items():
        print(key + ":" , value)

user = {"name":"John" , "age": 30 , "city":"New York" , "lang":"en"}
user_info(**user)