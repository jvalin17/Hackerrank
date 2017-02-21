
# coding: utf-8

# In[ ]:

N = int(raw_input())
lst = raw_input().split(' ')
lst = [int(num) for num in lst]
q = int(raw_input())


for i in range(q):
    x,y = raw_input().split(' ')
    x = int(x)-1
    y = int(y)-1
    
    if lst[x] % 2 != 0:
        print 'Odd'
    elif x == y:
        print 'Even'
    elif lst[x+1] == 0:
        print 'Odd'
    else:
        print 'Even'

