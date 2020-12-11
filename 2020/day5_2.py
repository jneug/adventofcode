from math import floor, ceil

input = []
with open('day5_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())


def get_row( r, low=0, high=127 ):
    if len(r) == 0 or low == high:
        return high
    else:
        if r[0] == 'F':
            return get_row(r[1:], low, floor((high+low)/2))
        else:
            return get_row(r[1:], ceil((high+low)/2), high)

def get_col( c, low=0, high=7 ):
    if len(c) == 0 or low == high:
        return high
    else:
        if c[0] == 'L':
            return get_col(c[1:], low, floor((high+low)/2))
        else:
            return get_col(c[1:], ceil((high+low)/2), high)

def get_seat( bpass ):
    row = get_row(bpass[:7])
    col = get_col(bpass[7:])
    return (row, col, row*8+col)

seats = []
for bpass in input:
    seats.append(get_seat(bpass))
seats.sort(key=lambda s: s[2])

for i in range(len(seats)-1):
    if seats[i][2]+1 != seats[i+1][2]:
        print(seats[i][2]+1)
        break