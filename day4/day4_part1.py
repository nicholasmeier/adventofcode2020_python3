# Goal : find # of valid passports
import sys
def Main():
    f = open("input.txt", "r")

    byr = 0
    iyr = 0
    eyr = 0
    hgt = 0
    hcl = 0
    ecl = 0
    pid = 0
    
    validcnt = 0
    while True:
        line = f.readline()
        if not line:
            break
        
        # okay, I know the correct value is 219 because the site tells you if your value needs to be higher or lower
        # But, the caveat to this is that I'm getting this weird error
        # I'm not sure what the issue is but I'm going to 
        
        # With the code here: the value returned is 220
        #if (byr == 1 and iyr == 1 and eyr == 1 and hgt == 1 and hcl == 1 and ecl == 1 and pid == 1):
            #validcnt += 1
        if line == '\n':
            # With the code here: the value returned is 218
            if (byr == 1 and iyr == 1 and eyr == 1 and hgt == 1 and hcl == 1 and ecl == 1 and pid == 1):
                validcnt += 1
            byr = 0
            iyr = 0
            eyr = 0
            hgt = 0
            hcl = 0
            ecl = 0
            pid = 0
        else:
            ls = line.split(" ")
            for l in ls:
                if l[0:3] == "byr":
                    byr += 1
                if l[0:3] == "iyr":
                    iyr += 1
                if l[0:3] == "eyr":
                    eyr += 1
                if l[0:3] == "hgt":
                    hgt += 1
                if l[0:3] == "hcl":
                    hcl += 1
                if l[0:3] == "ecl":
                    ecl += 1
                if l[0:3] == "pid":
                    pid += 1
    print(validcnt)

if __name__ == '__main__':
    Main()