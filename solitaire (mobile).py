from random import *

dictionary={}
fake=['xK','xQ','xJ','x10','x9','x8','x7','x6','x5','x4','x3','x2','xA']
sunny=['xK','xQ','xJ','x10','x9','x8','x7','x6','x5','x4','x3','x2','xA']
sunny=sunny+sunny+sunny+sunny+sunny+sunny
counter=0
#print len(sunny)



for a in range(len(fake)):
    dictionary[fake[a]]=a


fake=fake+fake
extra_card=[]


L1=[]
L2=[]
L3=[]
L4=[]
L5=[]
L6=[]
L7=[]
L8=[]


########################################################################

def instructions():
    print'''
INSTRUCTIONS
============

This Mobile Version so only one suit.
54 cards arranged in 8 columns and 24 extra card total 78 cards.
Game rules are same.
Here diff colours are indicated by diff variables like w,x,y,z
single move controls= a b c
a=serial no  b=initial column no  c=final column no
collection move controls= a b c d
a=serial no  b=initial column no  c=no of cards  d=final column no
extra card controls=a
a=serial no

'''
def cultivate1():
    global L1,L2,L3,L4,L5,L6,L7,L8,sunny
    c=0
    d=1
    l=[L1,L2,L3,L4,L5,L6,L7,L8]
    while True:
        b=randint(0,len(sunny)-1)
        if sunny[b] not in l[c]:
            l[c].append(sunny[b])
            del sunny[b]
            d+=1
        c+=1
        if c>7:
            c=0
        if d>54:
            break

def cultivate2():
    global sunny,extra_card
    while len(sunny)>0:
        
        b=randint(0,len(sunny)-1)
        extra_card.append(sunny[b])
        del sunny[b]

    
    
def display():
    global L1,L2,L3,L4,L5,L6,L7,L8
    l=[L1,L2,L3,L4,L5,L6,L7,L8]
    g=0
    t=max(len(L1),len(L2),len(L3),len(L4),len(L5),len(L6),len(L7),len(L8))
    print '\n\tDEEK'
    print
    for a in range(1,9):
        print a,'\t',
    print '\n'
    for a in range(t):
        for b in l:
            try:
                print b[g],'\t',
            except:
                print ' ','\t',
        print
        g+=1

def eliminate(x):
    global counter
    for i in range(len(x)):
        try:
            if ((((x[i]+x[i+1]+x[i+2]+x[i+3]+x[i+4]+x[i+5]+x[i+6]+x[i+7]+x[i+8]+x[i+9]+x[i+10]+x[i+11]+x[i+12]).replace('x','')).replace('y','')).replace('w','')).replace('z','')=='KQJ1098765432A':
                for a in range(13):
                    del x[i]
                counter+=1
        except:
            continue
    return x

def checkwin():
    global L1,L2,L3,L4,L5,L6,L7,L8
    if L1+L2+L3+L4+L5+L6+L7+L8==[]:
        return True
    


def single_move(a):
    global L1,L2,L3,L4,L5,L6,L7,L8,dictionary
    l=[L1,L2,L3,L4,L5,L6,L7,L8]
    b=a.split()
    del b[0]
    c=int(b[0])
    d=int(b[1])
    if l[c-1][-1][0]!=l[d-1][-1][0] or dictionary[l[c-1][-1]] - dictionary[l[d-1][-1]] not in [-1,1]:
        4/0
    else:
        
        e=l[c-1].pop()
        l[d-1].append(e)
        

def collection_move(a):
    global L1,L2,L3,L4,L5,L6,L7,L8
    l=[L1,L2,L3,L4,L5,L6,L7,L8]
    b=a.split()
    del b[0]
    c=int(b[0])
    d=int(b[1])
    e=int(b[2])
    q=-1
    p=l[c-1][q][0]
    print p
    for g in range(d):
        if p!=l[c-1][q][0]:
            4/0
        q-=1
    tmp=[]
    for f in range(d):
        tmp.append(l[c-1].pop())
    tmp.reverse()
    
    l[e-1].extend(tmp)

def extra():
    global extra_card,L1,L2,L3,L4,L5,L6,L7,L8
    l=[L1,L2,L3,L4,L5,L6,L7,L8]
    for i in l:
        i.append(extra_card.pop(0))
    
    



    
def menu1():
    print'''
MENU
====

1. NEW GAME
2. INSTRUCTIONS
3. EXIT

'''

def menu2():
    global extra_card,counter
    print'''

1. SINGLE MOVE
2. COLLECTION MOVE
3. EXTRA CARD'''
    print
    print 'Extra ',len(extra_card),' cards.'
    print
    print counter,' set packed.'
    print

###################################################################

##construct1()
##construct2()    

'''
for i in [L1,L2,L3,L4,L5,L6,L7,L8,L9,L10]:
    print i

print
display()
'''

print'''
=====================
SPIDER SOLITIARE GAME
=====================
    <mobile version>
         @ tamojitdas

'''

while True:
    menu1()
    a=input('>>> ')

    if a==2:
        instructions()
        raw_input('<= BACK ')
    elif a==3:
        print'\nGetting Out.\n'
        print'<tamojitdas>\n'
        raw_input()
        exit()
    elif a==1:
        
        
        
        
        
        cultivate1()
        #print len(L1+L2+L3+L4+L5+L6+L7+L8)
        cultivate2()
        #print len(extra_card)
            
        while True:
            display()
            print
            menu2()
            b=raw_input('>>> ')
            if b[0]=='1':
                try:
                    single_move(b)
                except:
                    print'\nInvalid'
            elif b[0]=='2':
                try:
                    collection_move(b)
                except:
                    print'\nInvalid'
            elif b[0]=='3':
                try:
                    extra()
                except:
                    print'\nInvalid'
    
            
            eliminate(L1)
            eliminate(L2)
            eliminate(L3)
            eliminate(L4)
            eliminate(L5)
            

            if checkwin():
                print'\n\tPLAYER WINS!'
                break
