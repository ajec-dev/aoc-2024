with open('input_2.txt', 'r') as file:
    lines = file.readlines()

def validate(levels: list[int]):
    direction = 0
    prev = 0
    for idx, num in enumerate(levels):
        if idx == 0:
            prev = num
        else:
            diff = num - prev
            sameDirection = direction * diff > 0
            if direction == 0:
                direction = diff
                sameDirection = True
            if abs(diff) < 1 or abs(diff) > 3 or sameDirection == False:
                return False
            prev = num
    return True

count = 0
for line in lines:
    nums = [int(num) for num in line.split()]
    if validate(nums):
        count += 1

print(count)