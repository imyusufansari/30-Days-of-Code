#In Python 3
#Solution of Anagram
#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/


for i in range(int(input())):
    s1=input()
    s2=input()
    a=[0]*26
    b=[0]*26
    k=[0]*26
    for j in range(len(s1)):
        temp=(ord(s1[j])%97)
        a[temp]+=1
    for j in range(len(s2)):
        temp=(ord(s2[j])%97)
        b[temp]+=1
    for j in range(len(a)):
        if(a[j]>b[j]):
            k[j]=a[j]-b[j]
        else:
            k[j]=b[j]-a[j]
    print(sum(k))
