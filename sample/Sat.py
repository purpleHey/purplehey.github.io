#!/bin/python3

import sys

# if __name__ == "__main__":
#     meal_cost = float(input().strip())
#     tip_percent = int(input().strip())
#     tax_percent = int(input().strip())

indexCount = 0
word = 'Howdy'

for index, letter in enumerate(word):
    print(index, letter)

myList1 = [1,2,3,4, 5, 6, 7]

for item in zip(myList1, myList1[1:], myList1[2:]):
    print(item)

results = []
for item in myList1:
    if item %2:
        results.append(item**2)
    else:
        results.append('Odd')

print(results)

st = 'Print only the words that start with s in this sentence'

for word in st.split(' '):
    if word[0] == 's':
        print(word)

for num in range(11):
    if not(num % 2):
        print(num)

list = [num for num in range(51) if num % 3 == 0]
print(list)

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split(' '):
    if len(word) % 2 == 0:
        print(word)

# Write a program that prints the integers from 1 to 100. But for multiples
# of three print "Fizz" instead of the number, and for the multiples of
# five print "Buzz". For numbers which are multiples of both three and
# five print "FizzBuzz".

for num in range(1,16):
    divby3 = num % 3 == 0
    divby5 = num % 5 == 0
    if divby3 and divby5:
        print('FizzBuzz')
    elif divby3:
        print('Fizz')
    elif divby5:
        print('Buzz')
    else:
        print(num)

letters = []
st = 'Create a list of the first letters of every word in this string'
# for word in st.split(' '):
#     letters.append(word[0]) 

# print(letters)
        
list = [letters[0] for letters in st.split(' ')]
print(list)