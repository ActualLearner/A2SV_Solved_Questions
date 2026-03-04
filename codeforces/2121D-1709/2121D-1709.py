# sort nums_a while recording the operations
    i = 0
    end = 0
    for i in range(n):
        for j in range(1, n - i):
            if nums_a[j-1] > nums_a[j]:
                nums_a[j], nums_a[j-1] = nums_a[j-1], nums_a[j]
                oprs.append([1, j])

    # sort nums_b while recording the operations
    i = 0
    end = 0
    for i in range(n):
        for j in range(1, n - i):
            if nums_b[j-1] > nums_b[j]:
                nums_b[j], nums_b[j-1] = nums_b[j-1], nums_b[j]
                oprs.append([2, j])

    for i in range(n):
        if nums_a[i] > nums_b[i]:
            nums_a[i], nums_b[i] = nums_b[i], nums_a[i]
            oprs.append([3, i+1])

    print(len(oprs))
    for o in oprs:
        print(*o)