import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')

    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb =  pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb


# write the data into person db
def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()


def doScoreDB(scdb):
    while(True):
        inputstr = (input("Score DB > "))
        if inputstr == "": continue
        parse = inputstr.split(" ")

        try:
            if parse[0] == 'add':
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
        except IndexError:
            print("IndexError")

        try:
            if parse[0] == 'del':
                for p in scdb[::-1]:
                    if p['Name'] == parse[1]:
                        scdb.remove(p)
        except IndexError:
            print("IndexError")

        try:
            if parse[0] == 'show':
                sortKey ='Name' if len(parse) == 1 else parse[1]
                showScoreDB(scdb, sortKey)
        except KeyError:
            print("KeyError")

        try:
            if parse[0] == 'find':
                for p in scdb:
                    if p['Name'] == parse[1]:
                        for attr in sorted(p):
                            print(str(attr) + "=" + str(p[attr]), end=' ')
                        print()
        except IndexError:
            print("IndexError")

        try:
            if parse[0] == 'inc':
                for p in scdb:
                    Score = int(p.get('Score'))
                    if p['Name'] == parse[1]:
                        p['Score'] = str(Score + int(parse[2]))
        except IndexError:
            print("IndexError")
        except ValueError:
            print("ValueError")

        if parse[0] == 'quit':
            break

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr + "=" + p[attr], end=' ')
        print()

scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
