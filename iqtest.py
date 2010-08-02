n = int(raw_input())
nums = raw_input()
# n = 4
# nums = "1 2 1 1"
nums = map(int, nums.split(" "))
#print nums

for i in range(-1, n-2):
  if (nums[i] % 2) is not (nums[i+1] % 2) and (nums[i] % 2) is not (nums[i-1] % 2):
    if i is -1:
      print n
      break
    else:
      print i + 1
      break