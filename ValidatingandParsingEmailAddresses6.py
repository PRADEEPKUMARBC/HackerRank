# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
N = int(input())
for _ in range(N):
    emls = email.utils.parseaddr(input())
    em = re.match(r"^[A-Za-z](\w|-|\.){1,}@([A-Za-z]{1,})\.[A-Za-z]{1,3}$",emls[1])
    if(em):
        print(email.utils.formataddr((emls[0],emls[1])))