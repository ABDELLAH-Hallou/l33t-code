# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(AA, AB, BB):
    aa_start = AA>0 and AA>=BB
    bb_start = BB>0
    if aa_start:
        mystring = "AA" 
        AA-=1 
    elif bb_start:
        mystring = "BB" 
        BB-=1
    else:
        return "".join(["AB" for i in range(AB)])
    
    while AA>0 or BB>0:
        if mystring[-1]=="A":
            if BB>0:
                mystring+="BB"
                BB-=1
            else:
                break
        else:
            if AA>0:
                mystring+="AA"
                AA-=1
            else:
                break
    
    for i in range(AB):
        if mystring[-1] != "A":
            mystring+="AB"
        elif mystring[0] != "B":
            mystring="AB"+mystring

    return mystring