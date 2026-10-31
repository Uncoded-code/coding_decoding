# import random
final=[]
st=input("enter the santence")
words=st.split(" ")
what=int(input("enter 0 for coding or 1 for decoding"))
what=True if what==0 else False
print(what)
if(what):
    for word in words:
        if(len(word)>=3):
            v1="hkf"
            # y1=random.join(v1)
            v2="wgc"
            # y2=random.join(v2)
            stn=v1+word[1:]+word[0]+v2
            final.append(stn)

        else:
            stn=word[::-1]
            final.append(stn)
        
else:
    for word in words:
        if(len(word)>=3):
            stn=word[3:-3]
            stn=stn[-1]+stn[0:-1]
            final.append(stn)
        else:   
            stn=word[::-1]
            final.append(stn)


print(" ".join(final))
       