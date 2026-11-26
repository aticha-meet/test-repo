# list_number = [1, 1, 3, 4, "Hello World"]

# print(list_number[2], "\n\n")
# print(list_number[4], "\n\n")

# print(list_number[1:4], "\n\n")

# print(list_number[1:5:2], "\n\n")

# print(f"Old list : {list_number} ")

# list_number.append(7)
# list_number.insert(3, "Index3")
# list_number.remove("Index3")

# print(f"New list : {list_number} \n\n")

# list_number.pop()
# print(f"New List After Pop : {list_number}")

# amount_of_list = len(list_number)
# print(f"Amount of List : {amount_of_list}")

# dict_data = {"hello": "World", 1: "Jaosou", "male": True}

# print(f"{dict_data['hello']}")
# print(f"{dict_data.get(1)}\n\n")

# print(f"Dict : {dict_data}")

# dict_data.pop("male")
# dict_data["newKey"] = "New World"
# dict_data.update({1: "Hello World 1"})
# dict_data.update({2: 3})

# print(f"New Dict : {dict_data}\n\n")

# print(f"{dict_data.items()}\n")
# for key, value in dict_data.items():
#     print(f"Key : {key}  Value : {value}\n")

# set_data = {1, 2, 3, 4}
# list_data = [1, 2, 1, 2, 3, 4, 4, 2, 1]

# print(f"Set : {set_data}")
# print(f"List : {set(list_data)}")

nums = [1, 6, 8, 11]

res = [x * 2 for x in nums if x > 6]
print(res)
