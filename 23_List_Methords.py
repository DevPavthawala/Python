l = [1,2,3,5,6,1,19,8,7]
# l.append(55)
# l[0]= 45
# l.sort()
# l.sort(reverse=True)
# print(l.index(1))
# print(l.count(1))

# m = l.copy()
# m[0] = 0
# print(m)
# print(l)

# m = l #not recommended as it print same
# m[0] = 0
# print(m)
# print(l)

l.insert(1,100)
print(l)

m = [900,1000,1100]
k = l+m # dont change l
l.extend(m) #change l
print(l)
print(k)