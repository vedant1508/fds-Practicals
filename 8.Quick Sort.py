def quick_sort(a,left,right):
    if left<right:
        partition_pos=partition(a,left,right)
        quick_sort(a,left,partition_pos-1)
        quick_sort(a,partition_pos+1,right)
def partition(a,left,right):
    i=left
    j=right
    pivot=a[right]

    while i<j:
        while i<right and a[i]<pivot:
            i+=1
        while j>left and a[j]>=pivot:
            j-=1
        if i<j:
            a[i],a[j]=a[j],a[i]
    if a[i]>pivot:
        a[i],a[right]=a[right],a[i]
    return i
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
quick_sort(a,0,len(a)-1)
print("Sorted Array=",a)
top()
