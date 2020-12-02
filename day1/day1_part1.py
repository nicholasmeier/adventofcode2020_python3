# Goal : find the two entries that sum to 2020, multiply them together to get the answer
def Main():
    f = open("input_d1.txt", "r")
    ents = []
    while True:
        line = f.readline().strip()
        ents.append(line)
        if not line:
            break
    ents.sort()
    ents.remove('')

    for x in range(len(ents)):
        for y in range(1, len(ents)):
            #print (ents[x] + " " + ents[y])
            #print (int(ents[x])+int(ents[y]))
            if int(ents[x])+int(ents[y]) == 2020:
                print(ents[x] + " " + ents[y])
                print (int(ents[x])*int(ents[y]))
        
    

if __name__ == '__main__':
    Main()