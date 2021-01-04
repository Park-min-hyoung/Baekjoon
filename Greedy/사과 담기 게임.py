import sys
input = sys.stdin.readline

n, m = map(int, input().split())
j = int(input())
nums = []

for i in range(j): nums.append(int(input()))

count = 0
left = 1
right = left + (m - 1)

for i in range(len(nums)):
    if left <= nums[i] <= right:
        continue
    if nums[i] > right:
        temp = abs(nums[i] - right)
        count += temp
        left += temp
        right += temp
    if nums[i] < left:
        temp = abs(nums[i] - left)
        count += temp
        left -= temp
        right -= temp
print(count)

# 틀렸음
'''나의 풀이 : 못풀었다 해답에 대한 발상자체를 못했다'''
'''아이디어: 1. left와 right로 나누기 2. 배열안의 수가 left와 right 사이라고 하면 당연히 옮길 필요없으니 continue
3. 배열안의 수가 right 보다 크면 움직인 거리만큼 더해주고 left와 right도 거리만큼 더해준다.
4. 배열안의 수가 left 보다 작으면 움직인 거리만큼 빼주고 left와 right도 거리만큼 빼준다.'''