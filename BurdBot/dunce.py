#sentance = input('Enter sentance:\n')

def duncey (sent):  
    res = ""    
    for idx in range(len(sent)):
        if not idx % 2 :
            res = res + sent[idx].upper()
        else:
            res = res + sent[idx].lower()
    return(res)

# printing result
# print("The alternate case string is : " + dunst(sentance))



#input() 
