import random
name_input = input("Enter names separated by comma\n")
name_list = name_input.split(", ")
total = len(name_list)
name = name_list[random.randint(0, (total-1))]
print(f"{name} will pay the bill")
