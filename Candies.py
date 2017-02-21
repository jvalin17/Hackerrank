
# coding: utf-8

# In[ ]:

n = int(raw_input())
arr = []
c = [1]*n
for i in range(n):
    arr.append(int(raw_input()))
    

for i in range(1,len(arr)):
    
    if arr[i-1] < arr[i]:
        c[i] = c[i-1]+1
        
for i in range(n-2,-1,-1):
    if arr[i] > arr[i+1]:
        c[i] = max(c[i],c[i+1]+1)

print sum(c)

