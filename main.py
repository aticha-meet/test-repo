print("Hello World\n")

age = 22
print("อายุ : ", age)
print(f"อายุ : {age}")

print("ใส่อายุ : ")
age_new = input()

name = input("ใส่ชื่อ : ")
print(f"ชื่อ : {name}\nอายุ : {age_new}")

s = "Hello World" #String(str)
number1 = 10 #Integer(int)
bath = 100.20 #Float(float)
value = True #Boolean(bool) True/False

print(type(s))
print(type(number1))
print(type(bath))
print(type(value))

number_string="10"
result = number1 + int(number_string)
print(result)
print(int(2.55555555555555555))


age1 = int(input("Enter Age : "))

if age1 <= 18:
    print("เด็ก")
elif age1 <= 30:
    print("ยังแจ๋ว")
else:
    print("ผู้ใหญ่")