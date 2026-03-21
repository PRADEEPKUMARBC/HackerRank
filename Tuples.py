n = int(input())
numbers = map(int, input().split())

t = tuple(numbers)
h = hash(t)
print(abs(h))
