# Goal : find the trees
import sys
def Main():
    f = open("input_d3.txt", "r")
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    
    mtn = f.read().splitlines()
    

    t_cnt=1
    for s in slopes:
        i = 0
        j = 0
        cnt = 0
        s_x = s[0]
        s_y = s[1]
        while True:
            j += s_y
            i += s_x
            if j >= len(mtn):
                break
            if (i >= len(mtn[j])):
                i = 0+(i-len(mtn[j]))
            if mtn[j][i] == '#':         
                cnt += 1
        t_cnt *= cnt
    print(t_cnt)

if __name__ == '__main__':
    Main()