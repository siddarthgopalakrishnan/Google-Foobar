def answer(xs):
    if len(xs) == 0:
        return str(0)
    if len(xs) == 1:
        return str(xs[0])

    # split input into positives and negatives
    positives = []
    negatives = []
    for i in xs:
        if i > 0: positives.append(i)
        elif i < 0: negatives.append(i)

    pcount = len(positives)
    ncount = len(negatives)

    if ncount == 1 and pcount == 0:
        return str(0)

    if ncount == 0 and pcount == 0:
        return str(0)

    maxprod = 1L
    for i in positives:
        maxprod *= i

    if ncount % 2 == 1:
        negatives.remove(max(negatives))

    for i in negatives:
        maxprod *= i

    return str(maxprod)