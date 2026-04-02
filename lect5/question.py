n = int(input())
arr = input().split(" ")
for i in range(len(arr)):
  arr[i] = int(arr[i])

arr.sort()
ans = []
for i in range(n-3):
  while(i< n-3 and arr[i]==arr[i+1]):
    i += 1
  j,k = i+1,n-1
  
  while(j<k):
    if(arr[i]+arr[j]+arr[k]==0):
      ans.append([arr[i],arr[j],arr[k]])
      while(j<k and arr[j]==arr[j+1]):
        j += 1
      j += 1
      while(j<k and arr[k]==arr[k-1]):
        k -= 1
      k -= 1
    if(arr[i]+arr[j]+arr[k]>0):
      k -= 1
    if(arr[i]+arr[j]+arr[k]<0):
      j += 1

print(ans)