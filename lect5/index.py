
n = int(input())
"1 -1 4 -5 6".split(" ")      # ["1","-1","4","-5","6"]
arr = input().split(" ")

for i in range(len(arr)):
  arr[i] = int(arr[i])

print(arr)