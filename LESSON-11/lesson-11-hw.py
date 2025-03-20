file = open('LESSON-11/numbers.txt', 'r')
nums = []
for content in file:
    nums.append(int(content.strip()))
file.close()

print(nums)
print(sum(nums))