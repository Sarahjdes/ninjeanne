import csv         # import csv module
import pprint
import json

# ele.csv       ele | fName | lName
# ens.csv       ens | fName | lName
# cours.csv     ens | title | group
# ins.csv       ele | group

def parse(whichList):

    result = []

    for row in whichList:
        result.append(row)

    return result

## setup  ##
f1 = open('ele.csv')
list_ele = parse(csv.reader(f1))

f2 = open('ens.csv')
list_ens = parse(csv.reader(f2))

f3 = open('cours.csv')
list_cours = parse(csv.reader(f3))

f4 = open('ins.csv')
list_ins = parse(csv.reader(f4))

#init error return values
errors = {
    'errors_subscribed_missing_students': [],
    'errors_subscribed_missing_courses': [],
    'errors_lecturing_missing_teachers': [],
    'errors_duplicate_students': [],
    'errors_duplicate_teachers': []
}

#isolate ins students and courses
ins_students = set()
ins_courses = set()
for ins in list_ins:
    ins_students.add(ins[0])
    ins_courses.add(ins[1])

#isolate ele students
ele_students = set()
for ele in list_ele:
    #Verify that there is no duplicates in list_ele
    if ele[0] in ele_students:
        errors['errors_duplicate_students'].append(ele[0])
    else:
        ele_students.add(ele[0])

#isolate cours courses and teachers
cours_courses = set()
cours_teachers = set()
for cours in list_cours:
    cours_courses.add(cours[2])
    cours_teachers.add(cours[0])

#isolate ens teachers 
ens_teachers = set()
for ens in list_ens:
    #Verify that there is no duplicates in list_ens
    if ens[0] in ens_teachers:
        #errors['errors_duplicate_teachers'].append(ens[0])
        errors['errors_duplicate_teachers'].append(ens)
    else:
        ens_teachers.add(ens[0])


## filtering ##

#Verify that every student in list_ins exist in list_ele
errors['errors_subscribed_missing_students'] = list(ins_students.difference(ele_students))

#Verify that every cours in list_ins exist in list_cours
errors['errors_subscribed_missing_courses'] = list(ins_courses.difference(cours_courses))

#Verify that every teacher in list_cours exist in list_ens
errors['errors_lecturing_missing_teachers'] = list(cours_teachers.difference(ens_teachers))
err_teach = errors['errors_lecturing_missing_teachers']

pp = pprint.PrettyPrinter(indent=4)
d = pp.pprint(errors)

with open('mycsvfile.csv','wb') as f:
    w = csv.writer(f)
    w.writerow(errors.keys())
    w.writerow(errors.values())

print errors['errors_subscribed_missing_courses']

print errors['errors_subscribed_missing_students']



if len(errors['errors_subscribed_missing_students']) != 0:
    print "missing students (%d):" % len(errors['errors_subscribed_missing_students'])

for x in errors['errors_subscribed_missing_students']:
    print x


if len(errors['errors_lecturing_missing_teachers']) != 0:
    print "missing teachers (%d):" % len(errors['errors_lecturing_missing_teachers'])

for x in errors['errors_lecturing_missing_teachers']:
    print x


if len(errors['errors_subscribed_missing_courses']) != 0:
    print "missing courses (%d):" % len(errors['errors_subscribed_missing_courses'])

for x in errors['errors_subscribed_missing_courses']:
    print x

