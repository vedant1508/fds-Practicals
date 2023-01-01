marklist=[]
n=int(input("Enter the Number of Students:"))
for i in range(n):
    mark=int(input(f"Enter the Marks of {i+1} Students:"))
    marklist.append(mark)
print(marklist)

#Avg
def avg():
    total=0
    for mark in marklist:
        total+=mark
    #print("Total=",total)
    print(f"Average Marks={total/len(marklist)}")


#min_max
def min_max():
    min=marklist[0]
    max=marklist[0]
    for mark in marklist:
        if mark<min:
            min=mark
        if max<mark:
            max=mark
    print(f"Highest Score={max} and Lowest Marks={min}")


#lowest Mark
"""def lowest():
    temp=[]
    for mark in marklist:
        if type(mark)==int:
            temp.append(mark)
    print(f"Lowest Mark={min(temp)}")
lowest()"""

#absent
def abs():
    absent=0
    for mark in marklist:
        if absent==0:
            absent+=1
    print(f"Absent Students={absent}")


#freq
def ff():
    freq={}
    for mark in marklist:
        if mark not in freq:
            freq[mark]=1
        elif mark in freq:
            freq[mark]+=1
    highest_freq=0
    highest_mark=0
    for mark in freq:
        if freq[mark]>highest_freq:
            highest_freq=freq[mark]
            highest_mark=mark
    print(f"Highest Frequency Marks={highest_mark} and Highest Frequency={highest_freq}")


choice=1
while(choice!=0):
    print("1.Average Marks\n2.Highest and Lowest Marks\n3.Absent\n4.Highest Marks Frequency\n5.Exit")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        avg()
    if choice==2:
        min_max()
    if choice==3:
        abs()
    if choice==4:
        ff()
    if choice==5:
        exit(0)
