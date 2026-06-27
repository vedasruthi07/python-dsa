 s=input()
freq={}
max_fre=0
ans=""
for i in s:
    freq[i]=freq.get(i,0)+1
    if freq[i]>max_fre:
        max_fre=freq[i]
        ans=i
print(ans)
l=list(map(int,input().split()))
seen=set()
for i in l: 
    if i in seen:
        print("duplicate found")
        break
    seen.add(i)
else:
    print("no dup")
s=input()
freq={}
for i in s:
    freq[i]=freq.get(i,0)+1
for i in s:
    if freq[i]>1:
        print(i)
        break
s=list(map(int,input().split()))
c=1 
l=1
for i in range(len(s)):
    if s[i]>s[i-1]:
        c+=1 
    else:
        l=1 
    l=max(l,c)
print(l)
li=list(map(int,input().split()))
l_sum=0
r_sum=0 
l=0
r=len(li)//2
for i in range(r):
    l_sum+=li[i]
    l+=1 
for j in range(r,len(li)):
    r_sum+=li[j]
    l+=1 
if l_sum==r_sum:
    print(i)
nums=list(map(int,input().split()))
target=int(input())
d={}
for i in range(len(nums)):
    need=target-nums[i]
    if need in d:
        print(d[need],i)
        break
    d[nums[i]]=i
    nums=list(map(int,input().split()))
f_l=nums[0]
s_l=float('-inf')
for i in range(1,len(nums)):
    if nums[i]>f_l:
        s_l=f_l 
        f_l=nums[i] 
    elif nums[i]>s_l:
        s_l=nums[i] 
print(f_l+s_l)
nums=list(map(int,input().split()))
min_price=nums[0]
max_pro=0 
for i in range(len(nums)):
    if nums[i]<min_price:
        min_price=nums[i] 
    else:
        profit=nums[i]-min_price 
        max_pro=max(max_pro,profit)
print(max_pro)
n=list(map(int,input().split()))
d={} 
for i in n:
    d[i]=d.get(i,0)+1 
for key in d:
    if d[key]>len(n)//2:
        print(key)
n=list(map(int,input().split()))
seen=set()
for i in n:
    if i in seen:
        print("True")
        break
    seen.add(i) 
else:
    print("False")
    nums=list(map(int,input().split()))
for i in range(len(nums)):
    p=1 
    for j in range(len(nums)):
        if i!=j:
            p*=nums[j]
    print(p,end=" ")
n=list(map(int,input().split()))
r=[1]*len(n)
p=1 
for i in range(len(n)):
    r[i]=p 
    p*=n[i] 
s=1 
for i in range(len(n)-1,-1,-1):
    r[i]=s 
    s*=n[i]
print(*r)
s=input()
stack=[]
d={
    ')' : '(',
    ']' : '[',
    '}' : '{',
}
for i in s:
    if i in "({[":
        stack.append(i)
    else:
        if not stack or stack[-1]!=d[i]:
            print("False")
            break 
        stack.pop()
else:
    print(not stack)
n=list(map(int,input().split()))
c=1 
m=1
v=sorted(set(n))
for i in range (1,len(v)):
    if n[i] - n[i-1] == 1:
        c+=1 
    else:
        c=1
    m=max(m,c)
print(m)
n=int(input())
for i in range(n):
    arr=list(map(int,input().split()))
    m=arr[0]
    nums=arr[1:]
    p_sum=0 
    for i in nums:
        p_sum+=i
        print(p_sum,end=" ")
    print()
m=int(input())
ans=[]
for i in range(m):
    arr=list(map(int,input().split()))
    v=arr[1:]
    p_sum=0
    res=[]
    for i in v:
        p_sum+=i 
        res.append(p_sum)
    ans.append((res))
for i in ans:
    print(*i)
m=int(input())
ans=[]
for i  in range(m):
    arr=list(map(int,input().split()))
    v=arr[1:]
    p_sum=0
    res=[]
    for i in v:
        p_sum+=i 
        if p_sum>0:
            res.append(p_sum)
    ans.append(res)
for i in ans:
    print(*i)
m=int(input())
for i in range(m):
    arr=list(map(int,input().split()))
    nums=arr[1:]
    t=0 
    fre={}
    for i in nums:
        if i in fre:
            t+=fre[i]
            fre[i]+=1 
        else:
            fre[i]=1 
    print(t)
v=int(input())
for i in range(v):
    arr=list(map(int,input().split()))
    s=arr[1:]
    res=[]
    ans=[]
    for i in s:
        b=str(i)
        if len(b)%2==0:
            res.append(b)
        
    print(*res)
v=int(input())
for i in range(v):
    arr=list(map(int,input().split()))
    s=arr[1:]
    res=[] 
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            s[i],s[i+1]=s[i+1],s[i] 
print(*s)
t=int(input())
for _ in range(t):
    arr=list(map(int,input().split()))
    nums=arr[1:]
    for i in range(1,len(nums)):
        k=nums[i]
        j=i-1 
        while j>=0 and nums[j]>k:
            nums[j+1]=nums[j]
            j-=1
        nums[j+1]=k
    print(*nums)
nums=list(map(int,input().split()))
nums=sorted(set(nums))
c=1
m=1
for i in range(1,len(nums)):
    if nums[i]-nums[i-1]==1:
        c+=1 
        m=max(m,c)
    else:
        c=1 
print(m)
l=list(map(int,input().split()))
k=int(input())
d={}
c=0
for i in l:
        d[i]=d.get(i,0)+1 
   # c+=1c=max(c,d[i]) 
print(d)
n=list(map(int,input().split()))
k=int(input())
d={}
for i in n:
    d[i]=d.get(i,0)+1 
result=sorted(d.items(),key=lambda x:x[1],reverse=True)
ans=[]
for i in range(k):
    ans.append(result[i][0]) # go to ith tuple and take 0 or 1 value 
print(*ans)
s=input()
l=0
seen=set()
m=0 
for r in range(len(s)):
    while s[r] in seen:
        seen.remove(s[l])
        l+=1 
    m=max(m,r-l+1) #window length
    seen.add(s[r])
print(m)
m=int(input())

for _ in range(m):
    v,s=map(int,input().split())
    a=list(map(int,input().split()))
    p=list(map(int,input().split()))
    i=0
    j=0
    ans=[]
    while i<v and j<s:
        if a[i]<=p[j]:
            ans.append(a[i])
            i+=1
        else:
            ans.append(p[j])
            j+=1

    while i<v:
        ans.append(a[i])
        i+=1 

    while j<s:
        ans.append(p[j])
        j+=1 

print(*ans)

m=int(input())
for _ in range(m):
    v,s=map(int,input().split())
    a=list(map(int,input().split()))
    left=a[:s+1]
    right=a[s+1:]
    i=0
    j=0 
    res=[]
    while i<len(left)and j<len(right):
        if left[i]<=right[j]:
            res.append(left[i])
            i+=1 
        else:
            res.append(right[j])
            j+=1 
    while i<len(left):
        res.append(left[i])
        i+=1
    while j<len(right):
        res.append(right[j])
        j+=1
for _ in range(m):
    print(*res)
        


    
        

        
    
    

    
