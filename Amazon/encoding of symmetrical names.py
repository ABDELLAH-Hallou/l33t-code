
def computeEncodedProductName(nameString):
    length = len(nameString)
    sorted_name = "".join(sorted(nameString))
    unique_chars = sorted(set(sorted_name))
    output={}
    result = [""]*length
    for character in nameString:
        if character in output:
            output[character]+=1
        else:
            output[character]=1

    ii = length-1
    i = 0
    for s in unique_chars:
        while output[s]>1:
            if output[s]==0:
                unique_chars.discard(s)
                ii-=1
                i+=1
                continue
            elif output[s] % 2 == 0 or output[s]>1:
                result[i], result[ii] == s,s
                output[s]-=s
            ii-=1
            i+=1
    for s in unique_chars:
        if output[s] == len([c for c in result if c==""]):
            for i,c in enumerate(result):
                if c=="":
                    result[i]=s
                    output[s]-=0
    return ''.join(result)