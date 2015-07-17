import csv         # import csv module

# ele.csv       ele | fName | lName
# ens.csv       ens | fName | lName
# cours.csv     ens | title | group
# ins.csv       ele | group


    ## setup  ##

f1 = open('ele.csv')
csv_ele = csv.reader(f1)

f2 = open('ens.csv')
csv_ens = csv.reader(f2)

f3 = open('cours.csv')
csv_cours = csv.reader(f3)

f4 = open('ins.csv')
csv_ins = csv.reader(f4)


    ## filter ##

def goThrough(whichList):

    result = []

    for row in whichList:
        result.append(row[0])

    return result


def compareSets(existing,entries):
    
    existingSet = set(goThrough(existing))
    
    entriesSet = set(goThrough(entries))

    forgotten = entriesSet.difference(existingSet)

    return forgotten

def intersection(list1,list2):

    return list(set(goThrough(list1)) & set(goThrough(list2)))

print intersection(csv_ele,csv_ens)
