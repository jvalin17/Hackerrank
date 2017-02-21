
# coding: utf-8

# In[ ]:

t = int(raw_input())
for i in range (t):
    n = int(raw_input())
    
    tot = 0
    buy = []
    sell = []
    stock_rate = raw_input().split(' ')
    
    for i in range(len(stock_rate)):
        stock_rate[i] = int(stock_rate[i]) 
     
    mx = 0
    i = len(stock_rate)-1
    while i >= 0:
        if stock_rate[i] >= mx:
            mx = stock_rate[i]
            
        tot = tot + (mx - stock_rate[i])
        i = i - 1
       
    print tot 

