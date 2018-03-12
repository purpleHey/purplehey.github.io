# def is_leapyear(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             return False
#         return True
#     return False

# for year in range(1900, 1910):
#     if is_leapyear(year):
#         print(f"{year} is a leap year - {year % 4}")

# Panda gram from file
my_file = open('input')

str1 = my_file.readline()

alphabet = "abcdefghijklmnopqrstuvwxyz"
lowerStr = str1.lower()
count = 0
for letter in alphabet:
    if lowerStr.count(letter):
        count = count + 1
    else:
        break

# print(f"Stopped at {alphabet[count]}")
print(count)
if count == 26:
    print("pangram")
else:
    print("no pangram")
