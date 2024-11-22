l1=[2,3,4,5,6,7,8,9,10]
l2=[1,2,3]

l3=list(set(l1)&set(l2))
print(l3)
'''
sm={1,2}
pm={2,3}
result=sm.intersection(pm)
print(result)
'''
maxNum=max(l1)
print(maxNum)

minNum=min(l1)
print(minNum)

# l1.append(l2)
# l1.insert(1,l2)
print(l1)
l3=l1
l3.reverse()

print("The reverse is", l1)

l5=[*l1,*l2]
print(l5)