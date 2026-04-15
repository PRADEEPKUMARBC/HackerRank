from collections import Counter

no_of_shoes = int(input())
list_of_shoes = list(map(int, input().split()))

counter_of_sizes = Counter(list_of_shoes)

no_of_customer = int(input())

total = 0

for customer in range(no_of_customer):
    size, price = map(int, input().split())
    
    if counter_of_sizes[size] > 0:
        total += price
        counter_of_sizes[size] -= 1

print(total)
