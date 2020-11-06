A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
if B1 <= C1 <= A1:
    A1, B1, C1 = A1, C1, B1
if C1 <= A1 <= B1:
    (A1, B1, C1) = (B1, A1, C1)
if B1 <= A1 <= C1:
    (A1, B1, C1) = (C1, A1, B1)
if A1 <= C1 <= B1:
    (A1, B1, C1) = (B1, C1, A1)
if A1 <= B1 <= C1:
    (A1, B1, C1) = (C1, B1, A1)
if B2 <= C2 <= A2:
    A2, B2, C2 = A2, C2, B2
if C2 <= A2 <= B2:
    (A2, B2, C2) = (B2, A2, C2)
if B2 <= A2 <= C2:
    (A2, B2, C2) = (C2, A2, B2)
if A2 <= C2 <= B2:
    (A2, B2, C2) = (B2, C2, A2)
if A2 <= B2 <= C2:
    (A2, B2, C2) = (C2, B2, A2)
if A1 == A2 and B1 == B2 and C1 == C2:
    if A1 + B1 + C1 == A2 + B2 + C2:
        print('Boxes are equal')
elif A1 <= A2 and B1 <= B2 and C1 <= C2:
    if A1 + B1 + C1 < A2 + B2 + C2:
        print('The first box is smaller than the second one')
elif A1 >= A2 and B1 >= B2 and C1 >= C2:
    if A1 + B1 + C1 > A2 + B2 + C2:
        print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
