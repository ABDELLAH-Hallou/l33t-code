class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        if x==y:
            return len(("AABB"*x)+("AB"*z))
        elif x>y:
            mystring = "AA" 
            x-=1 
        else:
            mystring = "BB" 
            y-=1

        while x>0 or y>0:
            if mystring[-1]=="A" and y>0:
                mystring+="BB"
                y-=1
            elif mystring[-1]=="B" and x>0:
                mystring+="AA"
                x-=1
            else:
                break
        
        for i in range(z):
            if mystring[-1] != "A":
                mystring+="AB"
            elif mystring[0] != "B":
                mystring="AB"+mystring

        return len(mystring)
