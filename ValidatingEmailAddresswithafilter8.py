import re
def fun(s):
    # return True if s is a valid email, else return False
    return bool(re.fullmatch(r"[\w-]+@[a-z0-9]+\.[a-z]{1,3}",s,re.I))

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)