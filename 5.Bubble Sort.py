def bubble_sort(a):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                print(f"Pass {i+1}=",a)
def top():
    b=[]
    for i in range(-5,0):
        b.append(a[i])
    print("Top 5 Records=",b)
a=[]
n=int(input("Enter the Number of Students:"))
for i in range(n):
    mark=float(input(f"Enter the Percentage of {i+1} students:"))
    a.append(mark)
print("Unsorted Array=",a)
bubble_sort(a)
print("Sorted Array=",a)
top()