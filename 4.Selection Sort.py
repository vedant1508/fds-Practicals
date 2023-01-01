def selection_sort(a):
    for i in range(len(a)):
        min_index=i
        for j in range(i,len(a)):
            if a[min_index]>a[j]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]
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
selection_sort(a)
print("Sorted Array=",a)
top()

