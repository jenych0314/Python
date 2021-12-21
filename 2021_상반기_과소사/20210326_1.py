import random

#2:중복
for i in range(5):
    n = random.randint(1,46)
    print(n)

#4: 중복
print(random.choices(range(1,47), k=5))

#1-1
nums1 = list(range(1,47))
print(random.sample(nums1,5))

#1-2
print(random.sample(list(range(1,47)),5))

#3-1
nums2 = set()
while True:
    n = random.randint(1,46)
    nums2.add(n)
    if len(nums2) == 5:
        break
print(nums2)

#3-2
nums2 = set()
while len(nums2) < 5:
    nums2.add(random.randint(1,46))
print(nums2)