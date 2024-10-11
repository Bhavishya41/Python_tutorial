x=int(input("press 1 for ENCODE or anyother number for DECODE :"))
if x == 1: 
 #Coding
    str = input("\nEnter the word to Code :")
    l = list(str)
    if len(str) >= 3:
        l2 = l[0]
        l = l[1:]
        l += l2
        ran = ['a', 'c', 'z']
        l += ran
        l[:0] = ran
        print("Output :",''.join(l),)
    else:
        l.reverse()
        print("Output :",''.join(l),)
#Decoding
else:
    str = input("\nEnter the word to Decode :")
    l = list(str)
    if len(str) <= 3:
        l.reverse()
        print("Output :",''.join(l),)
    else:
        l = l[3:-3]
        l2 = l.pop()
        l[:0] += l2
        print("Output :",''.join(l),)