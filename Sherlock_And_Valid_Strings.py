
# coding: utf-8

# In[ ]:

string = raw_input()

letter_box = {}
string_list = list(string)

for i in range(len(string_list)):
    curr = string_list[i]
    
    if curr in letter_box :
        letter_box[curr] += 1
    else:
        letter_box[curr] = 1
        

count= {}

for k,v in letter_box.items():
    if v in count:
        count[v] += 1
    else:
        count[v] = 1

if len(count) > 2:
    print 'NO'
elif len(count) == 1:
    print 'YES'
elif len(count) == 2:
    f = 0
    for k,v in count.items():
        if v == 1:
            f = 1
            break
    if f == 1:
        print 'YES'
    else:
        print 'NO'

