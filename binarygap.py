def solution(N):
    # write your code in Python 3.6
    ind = []
    mxln = 0
    if (isinstance(N, int) and (N in range(2147483647))):
        binum = str(bin(N))
        for each in range(len(binum)):
            if binum[each] == '1':
                ind.append(each)

        if len(ind) > 1:
            for i in range(len(ind) - 1):
                if ind[i + 1] - ind[i] > mxln:
                    mxln = ind[i + 1] - ind[i]
        if mxln <= 0:
            mxln = 0
        else:
            mxln = mxln - 1
    return mxln

solution(32)
solution(9)
solution(529)
