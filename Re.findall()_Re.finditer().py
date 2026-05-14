import re

t = re.findall(r"[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm][AEIOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",input())

if(t):
    for i in t:
        print(i[1:])
else:
    print(-1)