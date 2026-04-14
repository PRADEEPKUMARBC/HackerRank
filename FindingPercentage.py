if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    sum1 = float(sum(student_marks[query_name]))
    average = (sum1)/len(student_marks[query_name])
    qn_average = float(average)
    print(f"{qn_average:.2f}")
