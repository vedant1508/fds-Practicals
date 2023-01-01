marks=[]
n=int(input("Enter no. of Students : "))
def entry():
    for i in range (n):
        m=eval(input("Enter Marks: "))
        marks.append(m)
    print(marks)
def average():
    sum=0
    avg=0
    for i in marks:
        if type(i)==int:
            sum+=i
    avg=sum/n
    print("Average is :",avg)
def highest ():
    temp=[]
    for i in marks:
        if type(i)==int :
            temp.append(i)
    print("Maximum marks : ",max(temp))
def lowest():
    temp=[]
    for i in marks:
        if type(i)==int :
            temp.append(i)
    print("Minimum marks : ",min(temp))
def absent():
    count=0
    for i in marks:
        if i=="AB":
            count+=1
    print("Absent Students are : ",count)

def freq():
    freq={}
    for i in marks:
        if i not in freq:
            freq[i]=1
        else:
            freq[i]+=1
    m=max(freq,key=freq.get)
    print("Highest freqency : ",m)
    print("frequency : ", freq[m])

while (True):
    print("1.Entry\n2.Average\n3.Highest\n4.Lowest\n5.absent\n6.frequency")
    i=int(input("Enter Choice"))
    if i==1:
        entry()
    elif i==2:
        average()
    elif i==3:
        highest()
    elif i==4:
        lowest()
    elif i==5:
        absent()
    elif i==6:
        freq()
    else:
        print("Invalid Choice ")
        break
