#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from random import randint


all_objs = storage.all()
print("-- Reloaded objects --")
random_color = ""
reset = "\033[0m"
for obj_id in all_objs.keys():
    random_color = "\033[38;2;{};{};{}m".format(randint(50, 255),
                                                randint(50, 255),
                                                randint(50, 255))
    obj = all_objs[obj_id]
    print(random_color, end='')
    print(obj)
    print(reset, end='')


print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Holberton"
my_user.email = "airbnb@holbertonshool.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@holbertonshool.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)