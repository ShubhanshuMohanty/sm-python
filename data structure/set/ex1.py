#
my_set={1,"sj"}
print("my set=",my_set)
empty_set=set()
print("empty set=",empty_set)
my_set.add("sm")
print("my set=",my_set)
#clear
'''
my_set.clear()
print("my set=",my_set)
'''
#discard
my_set.discard("sj")
print("after removing sj, my set=",my_set)

a={1,2,3,4,5}   
b={4,5,6,7,8}
#intersection
print("intersection=",a.intersection(b))

#union
print("union=",a.union(b))

#difference
print("difference of a=",a.difference(b))
print("difference of b=",b.difference(a))

#symmetric difference
print("symmetric difference=",a.symmetric_difference(b))

#subset
print("a is subset of b=",a.issubset(b))

#superset
print("a is superset of b=",a.issuperset(b))

#pop
print("pop=",a.pop())
print("after pop=",a)
#frozenset
frozen_set=frozenset([1,2,3,4,5])
print("frozen set=",frozen_set)

sm={"name":"sm","age":22}
fset=frozenset(sm)