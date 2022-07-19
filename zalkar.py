##
##
##l = [2, 1, 3, 1, 1, 4]
##li = [0, 1, 2, 3, 4, 5]
##count = 0
##while li!=[]:
##    f = li[0]
##    diff = [(abs(l[f]-l[n]), n, lii) for lii, n in enumerate(li[1:], 0)]
##    print(diff)
##    s = min(diff)
##    print(s)
##    li.pop(s[2])
##    if len(li)!=1:
##        li.pop(0)
##    print(li)
##    print(f+1, s[1]+1)
###    count+=1
#
#
#
#l = [1, 4, 2, 5, 4, 2, 6, 3]
#li = [0, 1, 2, 3, 4, 5, 6, 7]
#
##l = input().split(' ')
##li = [i for i in range(l)]
#
#while li!=[]:
#    f = li[0]
##    print('f', f)
#    diff = [(abs(l[f] - l[num]), num) for num in li[1:]]
##    print(li)
#    s = min(diff)
##    print(s)
#    li.remove(s[1])
#    li.pop(0)
#    print(f+1, s[1]+1)
#
#
#
    
    
    # 2
#from collections import defaultdict
#nq = input().split()
#n = int(nq[0])
#q = int(nq[1])
##n, q = [int(n) for n in input().split()]
#db = dict()
#count = 0
#for i in range(q):
##    t, id = [int(n) for n in input().split()]
#    tid = input().split()
#    t = int(tid[0])
#    id = int(tid[1])
#    if t == 1:
#        count += 1
#        if id == 0:
#            # global notification
#            for i in range(1, n+1):
#                if i not in db:
#                    db[i] = list()
#                db[i].append(count)
#        else:
#            # personal notification
#            if id not in db:
#                db[id] = list()
#            db[id].append(count)
#    elif t == 2:
#        # display the last notification
#        print(db[id][-1] if (id in db and len(db[id])!=0)  else 0)
#    print(dict(db))


        
        
# 3

#def between(l, n):
#    for num in l:
#        if num != n:
#            return False
#    return True
#    
#def func(w):
#    if len(w) == set(w):
#        print('YES')
#    else:
#        s = set()
#        dupl = []
#        for i in range(len(w)):
#            if w[i] in s:
#                dupl.append((w[i], i))
#            else:
#                s.add(w[i])
#        flag = True
#        for d in dupl:
#            if not between(w[w.index(d[0]):d[1]+1], d[0]):
#                flag = False
#                break
#        print('YES' if flag else 'NO')
#    
#loop = input()
##w = [1, 1, 2, 3, 2]
#for i in range(int(loop)):
#    num_tasks = input()
#    w = input()
#    w = list(map(int, w.split()))
#    func(w)


#def any_friend(l1, l2):
    
    

from collections import defaultdict

mn = input().split()

m = int(mn[0])
n = int(mn[1])


friendship_dict = defaultdict(set)
for i in range(n):
    friends = input()
    friend_a, friend_b = friends.split(' ')[0], friends.split(' ')[1] #each line contains just two nodes separated by ;
    friendship_dict[friend_a].add(friend_b) # mutual friendship
    friendship_dict[friend_b].add(friend_a)

print(dict(friendship_dict))


for user, friends in friendship_dict.items():
    possible_friends = []
    for other in friendship_dict:
        if other != user:
            if len(friends.intersection(friendship_dict[other])) != 0:
                possible_friends.append((other,friends.intersection(friendship_dict[other])))
            print(possible_friends)
    print('-------------')
            
            
        





    
    
        

            
            
        
    




