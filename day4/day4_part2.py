# Goal : find # of valid passports with input validation
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

    # for ecl validation
    validEyes = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
    validHair = set('abcdef0123456789')

    debug = ''
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
        # print("byr: " + str(byr) + " iyr: " + str(iyr) + " eyr: " + str(eyr) + " hgt: " + str(hgt) + " hcl: " + str(hcl) + " ecl: " + str(ecl) +  " pid: " + str(pid))
        # print(debug)
        if line == '\n':
            debug = ''
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
                if l[-1] == '\n':
                    l = l.replace('\n','')
                debug += l + " "
                if l[0:3] == "byr" and int(l[4:]) >= 1920 and int(l[4:]) <= 2002:
                    byr += 1
                if l[0:3] == "iyr" and int(l[4:]) >= 2010 and int(l[4:]) <= 2020:
                    iyr += 1
                if l[0:3] == "eyr" and int(l[4:]) >= 2020 and int(l[4:]) <= 2030:
                    eyr += 1
                if l[0:3] == "hgt":
                    # print(l + " " + str(len(l)))
                    if l[-2:] == 'cm' and l[-6:-5] == ':' and l[-5:-4].isdigit() and int(l[-5:][:3]) >= 150 and int(l[-5:][:3]) <= 193:
                        hgt += 1
                    elif l[-2:] == 'in' and l[-5:-4] == ':' and len(l) == 8 and int(l[-4:][:2]) >= 59 and int(l[-4:][:2]) <= 76:
                        
                        hgt += 1
                if l[0:5] == "hcl:#" and len(l) == 11 and set(l[-6:]).issubset(validHair):
                    hcl += 1
                if l[0:3] == "ecl" and len(l) == 7 and (l[4:] in validEyes):
                    ecl += 1
                if l[0:3] == "pid" and len(l) == 13 and (l[4:].isnumeric()):
                    pid += 1
    print(validcnt)

if __name__ == '__main__':
    Main()