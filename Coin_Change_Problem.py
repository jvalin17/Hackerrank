
# coding: utf-8

# In[ ]:

n,m = map(int, raw_input().split(' '))
coins = map(int, raw_input().split(' '))

def makechange (all_coins,start,target,record):
    
    ways = 0
    amount = 0
    if n in record:
        return record[n]
    
    if target == 0:
        return 1
    
    if start >= len(all_coins):
        return 0
    
    
    key = str(target) + '-' + str(start)
    
    if key in record:
        return record[key]
    
    while amount <= target:
        
        ways = ways + makechange (all_coins,start+1,target-amount,record)
        amount = amount + all_coins[start]
        
    record[key] = ways
    return ways

record ={}
tot = makechange(coins,0,n,record)
print tot

