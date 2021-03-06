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


max_seat = 0
for bpass in input:
    seat = get_seat(bpass)
    if seat[2] > max_seat:
        max_seat = seat[2]
print(max_seat)