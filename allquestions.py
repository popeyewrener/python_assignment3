#program to check occurence of each element!!
print("QUESTION 1")
enter=input("Enter the string:")
string=enter
words=[]
letters=[]
count=0
dictionary={}

#spliting the string on all words available
words= string.split(" ")
if words[0] == string:
    for i in string:
        letters.append(i)
    for i in letters:
        if i in dictionary:
            #if word present their occurence will be added
            dictionary[i]+=1

        else:
            #if word not present than making element of dictionary
            dictionary[i]= 1
    

elif words == []:
    print("nil")

else:
    
    
    for i in words:
        if i in dictionary:
            #if word present their occurence will be added
            dictionary[i]+=1

        else:
            #if word not present than making element of dictionary
            dictionary[i]= 1


#printing occurence
if dictionary == {}:
    print("No values added")
for i in dictionary:
    print(i,":",dictionary[i])



#QUESTION 2
print("QUESTION 2")

day30=(4,6,9,11)
day31=(1,3,5,7,8,10,12)
day28=(2,)

day=int(input("Day- "))
month=int(input("Month- "))
year=int(input("Year-"))


if month > 12 or month <1  or day>31 or day<1:
    print("Invalid date")

elif year >2025 or year<1800 :
    print("Year outside range")   

elif month in day30:
    if day < 1 or day >30:
        print("Invalid date")

    elif day==30:
        print("Next date is:1/%s/%s"%((month+1),year))   

    else:
        print("Next date is:%s/%s/%s"%((day+1),(month),year))

elif month in day31:

    
    if day < 1 or day >31:
        print("Invalid date") 

    elif month == 12 and day == 31:
        print("Next date is:","1/1/%s"%((year+1)))     

    elif day==31:
        print("Next date is: 1/%s/%s"%((month+1),year))

    else:
        print("Next date is:%s/%s/%s"%((day+1),(month),year))    


elif month in day28:
    if year%4 == 0:
        if day < 1 or day >29:
            print("Invalid date") 

        elif day==29:
            print("Next date is: 1/%s/%s"%((month+1),year))   

        else:
            print("Next date is: %s/%s/%s"%((day+1),(month),year))  

    elif year%4 != 0:
        if day < 1 or day >28:
            print("Invalid date") 

        elif day==29:
            print("Next date is: 1/%s/%s"%((month+1),year))   

        else:
            print("Next date is: %s/%s/%s"%((day+1),(month),year))








#program to making a list of tuples of number and square of it
#defining input list
#default list
print("QUESTION 3")


inputList=[]

listsize=int(input("Enter number of elements in list: "))
for i in range (listsize):
    entry=float(input("Enter list:"))
    inputList.append(entry)


#taking output list as empty list
outputList=[]

for i in inputList:
    outputList.append((i,i*i))


print(outputList)    


#QUESTION 4
#program to take user grade points and priint their performance and grade

#taking given grade point values in a dictionary
print("QUESTION 4")
gradeLevel={10:["Outstanding","A+"],9:["Excellent","A"],8:['Very Good',"B+"],7:["Good","B"],6:["Average","C+"],5:["Below Average","C"],4:["Poor","D"]}

#asking user for grade point
gradePoint=int(input("Enter Grade: "))

#out of range part
if gradePoint >10 or gradePoint < (4):
    print("Grade out of range!!")


#in range part
elif gradePoint in gradeLevel:
    fetch=gradeLevel[gradePoint]
    letterGrade=fetch[1]
    performance=fetch[0]

    print("Your Grade is '%s' and %s Performance"%(letterGrade,performance))

#QUESTION 5
#program to print pattern in python

#given string stored
print("QUESTION 5")
string="ABCDEFGHIJK"


#loop for printing pattern runs!!!
for lim in range (11,0,-2):
    space=5-int(lim/2)
    
    print(" "*space+(string[0:lim]))
    

#QUESTION 6
#program to store data in dictionary

print("QUESTION 6")

studentDictionary={}

while True:
    name=input("Enter name: ")
    sid=int(input("Enter SID: "))
    studentDictionary[sid]=name
    choice=input("Want to enter more? ('Y' or 'N'): ")
    if choice.upper() == "N":
        break
    elif choice.upper() == "Y":
        continue
    else:
        print("Invalid choice")
        break


#part a
print("Part A \nPrinting student details!")
for i in studentDictionary:
    print("SID:",i,'Student Name:',studentDictionary[i])


#part B
print(" ")
print("part B\nSorting using student name!")
sortedList=[]
for i in studentDictionary:
    sortedList.append([studentDictionary[i],i])
    sortedList.sort()


for element in sortedList:
    print("SID:",element[1],"Name:",element[0])    


#part C
print(" ")
print("Part c\n Sorting by using SID")
sortedList=[]
for i in studentDictionary:
    sortedList.append([i,studentDictionary[i]])
    sortedList.sort()


for element in sortedList:
    print("SID:",element[0],"Name:",element[1])  


#part D
print(" ")
print("Part D\nSearching by SID")
search=int(input("Enter SID to search: "))
if search in studentDictionary:
    print("Student found!\nName:",studentDictionary[search])

else:
    print("No student records found")




#program for display of fibonacci series
#initialing variables to 0 anf first wo term as 0 and 1

print("QUESTION 7")
sum=0
a2=0
a0=0
a1=1

#taking user input

num=int(input("Enter the number upto which Fibo sequence will be printed: "))

#running loop
for i in range(num):
    print(a2)
    a2=(a0+a1)
    sum+=a2
    
    a0=a1
    a1=a2

#defining average
avg=(sum/num)
print("Average of series is:",avg)


#SET QUESTION
print("QUESTION 8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# part a
Set_Uni = Set1.union(Set2)
Set_Inter = Set1.intersection(Set2)
Part_A_Set = Set_Uni - Set_Inter
print("<PART a SET>", Part_A_Set)

# part b(Subtracting intersection of sets taken two at a time from the Union of all three sets)
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("<PART b SET>", Part_B_Set)

# part c(Subtracting the intersection of all three sets from the Intersection of sets taken two at a time)
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("<PART c SET>",Part_C_Set)
# part d(Excluding the numbers from 1 to 10 that are occuring in Set1)
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("<PART d SET>", Part_D_Set)
# part e(Excluding the numbers from 1 to 10 that are occuring in Set1, Set2 and Set3)
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("<PART e SET>", Part_E_Set)