# units holds single digit numbers to words
units = ["", "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine"]

# teens holds two digit numbers from 11 to 19 to words
teens = ["", "eleven", "twelve", "thirteen", "fourteen",
    "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

# tens holds zero trailing numbers to words
tens = ["", "ten", "twenty", "thirty", "forty",
    "fifty", "sixty", "seventy", "eighty", "ninety"]

# thousands holds more then two zero trailing number to words
thousands = ["", "thousand", "million", "billion", "trillion",
    "quadrillion", "quintillion", "sextillion", "sextillion", "octillion",
    "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion",
    "quattuordecillion", "sexdecillion", "septendecillion", "octodecillion",
    "novemdecillion", "vigintillion "]

# function number to word converts numbers to words
def numToWords(num):
    
    # words list
    words = []
    
    if num == 0:
        words.append("zero")
    else:
        
        # number to string
        numStr = str(num)
        
        # number of digit in number
        numStrLen = len(numStr)
        
        # number of groups can be created of the number.
        # each group can be of size 3
        groups = (numStrLen + 2) / 3
        
        # fill with initial zeros if the length is not multiple of 3
        numStr = numStr.zfill(groups * 3)
        
        # loop through each group
        for i in range(0, groups * 3, 3):
            h = int(numStr[i])
            t = int(numStr[i + 1])
            u = int(numStr[i + 2])
            g = groups - (i / 3 + 1)
            
            # Get number to string of hundreds place
            if h >= 1:
                words.append(units[h])
                words.append("hundred")
                if(not (t == 0 and u == 0)):
                    words.append("and")
            
            # get number to string of decimals place 
            if t > 1:
                # if t greater then 1 use tens variable to get the word
                words.append(tens[t])
                # append units word directly
                if u >= 1:
                    words.append(units[u])
            elif t == 1:
                
                # if t equal to 1 use teens to get the word
                # if u greater than or equal to 1 use teens to get word
                if u >= 1:
                    words.append(teens[u])
                else:
                    # else use tens to get word
                    words.append(tens[t])
            else:
                # go for units place if tens place is zero
                if u >= 1:
                    words.append(units[u])
            
            # append thousands when required 
            if g >= 1 and (h + t + u) > 0:
                words.append(thousands[g])
                
        # return list of words required        
        return words

# main called first when code is executed
if __name__ == '__main__':
    totalLength = 0
    for num in range(1,1001):
        totalLength += len("".join(numToWords(num)))
        
    #  print total length    
    print totalLength
