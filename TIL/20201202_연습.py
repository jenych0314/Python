# score = [88, 95,70,100,99]

# for no, s in enumerate(score, 1):
#     print(str(no) + "번 학생의 성적: ", s)

# yoil = ['월', '화', '수', '목', '금', '토', '일']
# food = ['갈비탕', '순대국', '칼국수', '삼겹살']

# menu = zip(yoil, food)

# for y, f in menu:
#     print("%s요일 메뉴: %s" %(y,f))

# nums = [n * 2 for n in range(1,11)]
# for i in nums:
#     print(i, end=' ')

# num = [n for n in range(1,11) if n % 3 == 0]
# for i in num:
#     print(i, end=' ')

# num = [n * n for n in range(1,11) if n % 3 == 0]
# for i in num:
#     print(i, end=' ')

# nums = [1,2,3,4]
# nums[2:2] = [90,91,92]
# print(nums)

# nums = [1,2,3,4]
# nums[2] = [90,91,92]
# print(nums)

# num1 = [1,2,3,4]
# num2 = [90,91,92]
# num1 += num2
# print(num1)

score = [88,95,70,100,99,35]
print(score.pop())
print(score.pop(3))