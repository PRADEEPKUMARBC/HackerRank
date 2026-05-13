# Enter your code here. Read input from STDIN. Print output to STDOUT

s = input()

for char in range(len(s)-1):
    if s[char].isalnum() and s[char] == s[char+1]:
        print(s[char])
        break
else:
    print(-1)