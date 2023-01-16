def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    res = ""
    n = len(s)
    cycle_len = 2 * numRows - 2
    for i in range(numRows):
        for j in range(i, n, cycle_len):
            res += s[j]
            if i != 0 and i != numRows-1 and j+cycle_len-2*i < n:
                res += s[j + cycle_len - 2 * i]
    return res


def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    res = [''] * numRows
    index, step = 0, 1

    for x in s:
        res[index] += x
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    return ''.join(res)
