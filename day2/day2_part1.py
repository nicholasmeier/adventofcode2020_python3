# Goal : find the passwords that are valid
import sys
def Main():
    f = open("input_d2.txt", "r")
    valid_cnt = 0
    while True:
        line = f.readline()
        if not line:
            break
        lines = line.split(':')
        password = (lines[1])
        password = password[1:]
        

        reqs = lines[0].split(' ')
        req_range = reqs[0]
        range_max = int(req_range.split('-')[1])
        range_min = int(req_range.split('-')[0])

        req_char = reqs[1]

        req_cnt = 0
        for c in password:
            if c == req_char:
                req_cnt+=1
        
        if ((req_cnt <= range_max) and (req_cnt >= range_min)):
            valid_cnt+=1
        
    print(valid_cnt)
    

if __name__ == '__main__':
    Main()