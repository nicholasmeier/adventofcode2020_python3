# Goal : find the trees
import sys
def Main():
    f = open("input_d3.txt", "r")
    s_x = 3
    s_y = 1
    
    mtn = f.read().splitlines()
    i = 0
    j = 0

    cnt = 0
    while True:
        j += s_y
        i += s_x
        if j >= len(mtn):
            break
        if (i >= len(mtn[j])):
            i = 0+(i-len(mtn[j]))
        if mtn[j][i] == '#':         
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    Main()