x = [1, 2, 3]
print(id(x))
print(id([1, 2, 3]))
y = x
print(id(y))
print(x is y)
print(y is [1, 2, 3])
x.append(4)
print(x)
print(y)
print(x is y)
print(id(y), id(x))
print(type(x))
print(type(4))
print(type(type(x)))

objects = [1, 2, 1, 2, 3]
ans = 0
ans_l = []
for obj in objects: # доступная переменная objects
    if ans_l.count(obj)<1:
        ans += 1
        ans_l.append(obj)

print(ans)
print(ans_l)
print("master")
print("3333")