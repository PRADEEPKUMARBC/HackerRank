# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input().strip())

for i in range(T):
    uuid = input().strip()
    
    is_valid = (
        len(set(uuid)) == 10
        and uuid.isalnum()
        and sum(c.isupper() for c in uuid) >= 2
        and sum(c.isdigit() for c in uuid) >= 3
    )

    print("Valid" if is_valid else "Invalid")