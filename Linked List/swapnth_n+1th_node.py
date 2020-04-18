# Enter your code here. Read input from STDIN. Print output to STDOUT
class node:
    def __init__(self,info):
        self.val=info
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def swap(self,n,k):
        for i in range(n-k):
            temp=temp.next
        x=temp.next.info
        temp.next.info=temp.next.next.info
        temp.next.next.info=x
        return
    def push(self,info):
        temp=node(info)
        if self.head==None:
            self.head=temp
            temp.next=self.head
            return
        temp2=self.head
        while(temp2.next):
            temp2=temp2.next
        temp2.next=temp
        print(temp.info)
        temp.next=None
        return
            
y=list(map(int,input().split()))
z=list(map(int,input().split()))
try1=llist()
print(z)
for _ in z:
    try1.push(_)


#try1.swap(y[0],y[1])

        