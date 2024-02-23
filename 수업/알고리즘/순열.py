for a in range(1, 4):
    for b in range(1, 4):
        if a != b :
            for c in range(1, 4):
                if a != c and b != c:
                    print(a, b, c)