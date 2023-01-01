def insertion_sort(a):
    i=1
    for i in range(n):
        temp=a[i]
        j=i-1
        while(j>=0)&(a[j]>temp):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=temp
def top():
    b=[]
    for i in range(-5,0):
        b.append(a[i])
    print("Top 5 Records=",b)
a=[]
n=int(input("Enter the number of students:"))
for i in range(n):
    mark=float(input(f"Enter the Percentage of {i+1} students:"))
    a.append(mark)
print("Unsorted Array=",a)
insertion_sort(a)
print("Sorted Array=",a)
top()