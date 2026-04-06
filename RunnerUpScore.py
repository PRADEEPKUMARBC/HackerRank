if __name__ == '__main__':
    n = int(input())
    l = map(int, input().split())
    s = set(l)
    l2 = list(s)
    
    l2.sort()
    print(l2[-2])
