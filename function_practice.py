def max_num(a, b, c):
    if a > b and a > c:
        print(a)
        return a
    elif b > a and b > c:
        print(b)
        return b
    elif c > a and c > b:
        print(c)
        return c


def mult_list(*args):
    num = 1
    for a in args:
        num *= a
    print(num)
    return num


def rev_string(string):
    newString = string[::-1]
    print(newString)
    return newString


def num_within(num, stRange, enRange):
    return num in range(stRange, enRange+1)


triangle = [[1], [1, 1]]


def pascal(n):
    # base case
    if n < 1:
        print("invalid number of rows")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        # fill up correct number of rows in triangle
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            # create correct row, then add to triangle (this row will be 1 longer than row before it)
            length = len(row_prev)+1
            for i in range(length):
                # first number is 1
                if i == 0:
                    row.append(1)
                # intermediate nunmbers get added from previous rows
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number-1]
                               [i-1]+triangle[row_number-1][i])
                # last number is 1
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        # print triangle
        for row in triangle:
            print(row)


max_num(2, 5, 14)

mult_list(4, 5, 2)

rev_string('david')

print(num_within(3, 2, 4))

triangle = [[1], [1, 1]]
print(triangle)
