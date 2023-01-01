def shell_sort(a,n):
    d=n//2
    while d>0:
        for i in range(d,n):
            temp=a[i]
            j=i
            while(j>=d)&(a[j-d]>temp):
                a[j]=a[j-d]
                j=j-d
            a[j]=temp
        d=d//2
def top():
    b=[]
    for i in range(-5,0):
        b.append(a[i])
    print("Top 5 Records=",b)
a=[]
n=int(input("Enter the Number of students:"))
for i in range(n):
    mark=float(input(f"Enter the Percentage of {i+1} students:"))
    a.append(mark)
print("Unsorted Array=",a)
shell_sort(a,n)
print("Sorted Array=",a)
top()


