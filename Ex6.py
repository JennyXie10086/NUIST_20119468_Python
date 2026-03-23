student_names = ["Jenny", "Liver", "Fiona", "Cici"]

# 遍历列表并输出名和姓
for name in student_names:
    print(f"First name: {name}, Last name: Example")

# 提示用户输入新名字
new_name = input("Enter another name to add: ")
student_names.append(new_name)

# 按姓氏排序并输出
student_names.sort()
print("Sorted list by last name:")
for name in student_names:
    print(f"{name} Example")
