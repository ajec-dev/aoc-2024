from collections import Counter

with open('input_1.txt', 'r') as file:
    col1nums = []
    col2nums = []
    for line in file:
        num1, num2 = map(int, line.split())
        col1nums.append(num1)
        col2nums.append(num2)

col2nums_counts = Counter(col2nums)

result = sum(num * col2nums_counts.get(num, 0) for num in col1nums)
print(result)
# output: 24931009