# Goal : find the three entries that sum to 2020, multiply them together to get the answer
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
            for z in range(2, len(ents)):
                if int(ents[x])+int(ents[y])+int(ents[z]) == 2020:
                    print(ents[x] + " " + ents[y] + " " + ents[z])
                    print (int(ents[x])*int(ents[y])*int(ents[z]))
        
    

if __name__ == '__main__':
    Main()