name=[]
time=[]
loc=[]
paid=[]
def push():
   a=input('enter name :')
   t=input('enter time:')
   l=input('enter location:')
   p=input('enter if paid or not')
   name.append(a)
   time.append(t)
   loc.append(l)
   paid.append(p)

def pop():
   name.pop(0)
   time.pop(0)
   loc.pop(0)
def queue():
 while len(name)<=2:
    ch=input('do you want to continue?')
    if ch=='yes':
        c=input('push or pop')
        if c=='pop':
         pop()
         print(name,time,loc)
        elif c=='push':
         if len(name)==2:
           print('queue full')
           continue
         else:
           push()
         print(name,time,loc,paid)
    else:
       print('quitting')
       break
queue()

for i in range(len(name)):
    l=[]
    l.append(name[i])
    l.append(time[i])
    l.append(loc[i])
    l.append(paid[i])
    print(l)

for i in range(len(name)):
    if paid[i]=='no':
        name.pop(i)
        time.pop(i)
        loc.pop(i)
        paid.pop(i)
        print(name,time,loc,paid)