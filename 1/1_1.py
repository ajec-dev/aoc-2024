with open('input_1.txt', 'r') as file:
    lines = file.readlines()

col1nums = []
col2nums = []
for line in lines:
    num1, num2 = map(int, line.split('   '))
    col1nums.append(num1)
    col2nums.append(num2)
col1nums.sort()
col2nums.sort()

sum = 0
for num1, num2 in zip(col1nums, col2nums):
    sum += abs(num1 - num2)

print(sum) 
# output: 2066446