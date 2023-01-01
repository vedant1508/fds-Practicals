r=int(input("Enter the number of Rows:"))
c=int(input("Enter the number of Columns:"))
a=[]
print("Enter the elements of 1st Matrix:")
for i in range(r):
    a.append([])
    for j in range(c):
        num=int(input())
        a[i].append(num)
b=[]
print("Enter the elements of 2nd Matrix.")
for i in range(r):
    b.append([])
    for j in range(c):
        num=int(input())
        b[i].append(num)

def add():
    sum=[]
    for i in range(r):
        sum.append([])
        for j in range(c):
            sum[i].append(a[i][j]+b[i][j])
    print("Addition of Matrix is:\n")
    for i in range(r):
        for j in range(c):
            print(sum[i][j],end=" ")
        print()
def subtract():
    sub=[]
    for i in range(r):
        sub.append([])
        for j in range(c):
            sub[i].append(a[i][j]-b[i][j])
    print("Subtraction\n")
    for i in range(r):
        for j in range(c):
            print(sub[i][j],end=" ")
        print()
def multiply():
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(r):
        for j in range(c):
            for k in range(r):
                result[i][j]+=a[i][k]*b[k][j]
    print("Multiplication\n")
    for i in result:
        print(i)
def transpose():
    result=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(a)):
        for j in range(len(a[0])):
            result[j][i]=a[i][j]
    for i in result:
        print(i)
choice=1
while(choice!=0):
    print("1.Addition\n2.Subtraction\n3.Multplication\n4.Transpose\n5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add()
    elif choice==2:
        subtract()
    elif choice==3:
        multiply()
    elif choice==4:
        transpose()
    elif choice==5:
        exit(0)