sentence=input("Enter the Sentence:")
sen=sentence.split()
print(sen)
choice=1
while(choice!=0):
    print("1.Longest Word\n2.Frequency Occurance of each character\n3.Palindrome\n4.Index of sub string\n5.Frequency Occurance of each word.\n6.Exit\n")
    choice=int(input("Enter your Choice:"))
    if choice==1:
        longest=max(sen,key=len)
        print(f"Longest Word={longest} and Longest Length={len(longest)} \n")
    elif choice==2:
        freq={}
        for i in sentence:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        print(f"Frequency Occourance of each Charater ={freq} \n")
    elif choice==3:
        sub=input("Enter the Sub String:")
        if sub==sub[::-1]:
            print(f"{sub} is Palindrome. \n")
        else:
            print(f"{sub} is not Palindrome. \n")
    elif choice==4:
        sub=input("Enter the Sub String:")
        x=sentence.find(sub)
        print(f"Sub String is present at {x} position. \n")
    elif choice==5:
        freq={}
        for i in sen:
            if freq in sen:
                freq[i]+=1
            else:
                freq[i]=1
        print(f"Frequency Occourance in each word is {freq}. \n")
    elif choice==6:
        exit(0)

