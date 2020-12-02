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
        
        pt1 = int(req_range.split('-')[0])-1
        pt2 = int(req_range.split('-')[1])-1

        req_char = reqs[1]

        if len(password) > pt2:
             if (req_char == password[pt1] and req_char != password[pt2]) or (req_char != password[pt1] and req_char == password[pt2]):
                 valid_cnt+=1
        
    print(valid_cnt)
    

if __name__ == '__main__':
    Main()