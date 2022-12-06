
## Read input file
input = []
with open('day6_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line)


# Solve problem
def find_marker( marker_length ):
    for i in range(len(input[0])-marker_length):
        if( len(set(input[0][i:i+marker_length])) == marker_length ):
            print(input[0][i:i+marker_length])
            print(i+marker_length)
            break



if __name__ == '__main__':
    find_marker(14)
