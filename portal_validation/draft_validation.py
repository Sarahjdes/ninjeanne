print "CSV validation"

import csv          # import csv module

# file1         ele | fName | lName
# file2         prof | fName | lName
# file3         prog | title | group
# file4         ele | group


    ## Unregristered students ##

f = open('1.csv')
csv_1 = csv.reader(f)

ele_1 = []

for row in csv_1:
    ele_1.append(row[0])
    

f = open ('4.csv')
csv_4 = csv.reader(f)

ele_4 = []

for row in csv_4:
    ele_4.append(row[0])

ele_1_set = set(ele_1)
ele_4_set = set(ele_4)

forgotten_ele = ele_4_set.difference(ele_1_set)

print 'unregistered students :'
print list(forgotten_ele)


    ## Unexisting groups ##

f = open('4.csv')
csv_4 = csv.reader(f)

group_4 = []

for row in csv_4:
    group_4.append(row[1])
    

f = open ('3.csv')
csv_3 = csv.reader(f)

group_3 = []

for row in csv_3:
    group_3.append(row[2])

group_4_set = set(group_4)
group_3_set = set(group_3)

forgotten_group = group_4_set.difference(group_3_set)

print 'unexisting groups :'
print list(forgotten_group)


    ## Unregistered teachers ##

f = open('3.csv')
csv_3 = csv.reader(f)

prof_3 = []

for row in csv_3:
    prof_3.append(row[0])
    

f = open ('2.csv')
csv_2 = csv.reader(f)

prof_2 = []

for row in csv_2:
    prof_2.append(row[0])

prof_3_set = set(prof_3)
prof_2_set = set(prof_2)

forgotten_prof = prof_3_set.difference(prof_2_set)

print 'unregistered teachers :'
print list(forgotten_prof)


    ## Teachers and students sharing same ID ##

sharing_ele_prof = []

for x in prof_2: 
    if (x in ele_1):
        sharing_ele_prof.append(x)

print 'teachers and student share same id :'
print list(sharing_ele_prof)

f = open ('1.csv')
csv_1 = csv.reader(f)

sharing_ele = []

for row in csv_1:
    if row[0] in sharing_ele_prof:
        sharing_ele.append(row)

if sharing_ele != []:
    print 'students with a student ID: '
    print list(sharing_ele)


f = open ('2.csv')
csv_2 = csv.reader(f)

sharing_prof = []

for row in csv_2:
    if row[0] in sharing_ele_prof:
        sharing_prof.append(row)

if sharing_prof != []:
    print 'teachers sharing a student ID: '
    print list(sharing_prof)


    ## Duplicate students IDs ##


f = open ('1.csv')
csv_1 = csv.reader(f)

duplicate_ele = set([x for x in ele_1 if ele_1.count(x) > 1])

print 'duplicate students ID :'
print list(duplicate_ele)


    ## Duplicate teachers IDs ##

duplicate_prof = set([x for x in prof_2 if prof_2.count(x) > 1])

print 'duplicate teachers ID :'
print list(duplicate_prof)
