import profile
def checkAndGiveAddition(parentList, childList):
    
    # dummy Data
    # parentList = [1,2]
    # childList = [1,2,3]
    
    # Dummy list to append to front for leftAddition and to append to back for rightAddition
    m = [0]
    
    # LeftAddition is [1,2,0] + [1,2,3] = [2,4,3]
    leftAddition = [l+r for l,r in zip(parentList+m, childList)]
    
    # RightAddition is [0,1,2] + [1,2,3] = [1,3,5]
    rightAddition = [l+r for l,r in zip(m+parentList, childList)]
    
    # returns max([2,4,3], [1,3,5]) = [2,4,5]
    return [max(l,r) for l,r in zip(leftAddition, rightAddition)]

 
def mainLogic():   
    # initially list is empty
    previousList = []
    
    # loop through all the data in file
    for line in open('datafile.txt', 'r'):
        
        # Get single line of data and convert it into list
        dataLine = [int(x) for x in line.split()]
        
        # no nothing for empty previousList
        if(previousList!=[]):
            previousList = checkAndGiveAddition(previousList, dataLine)
        else:
            previousList = dataLine
            
    print max(previousList)
    
    
# main called first when code is executed
if __name__ == '__main__': 
    profile.run("mainLogic()") 

    