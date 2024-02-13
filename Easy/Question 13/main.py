
def searchNumerals(var):
    NumeralArray = ["I", "V", "X", "L", "C", "D", "M"]
    count = 0
    for i in NumeralArray:        
        if var == i:
            return count    
        count += 1

def convertToInt(s):

    ValueArray = [1,5,10,50,100,500,1000]
    
    returnCount = 0
    for i in range(len(s)):
        try:
            if searchNumerals(s[-i-1]) > searchNumerals(s[-i-2]):
                returnCount += ValueArray[searchNumerals(s[-i-1])]-ValueArray[searchNumerals(s[-i-2])]
                returnCount -= ValueArray[searchNumerals(s[-i-2])]
            else:
                returnCount += ValueArray[searchNumerals(s[-i-1])]
        except:
            returnCount += ValueArray[searchNumerals(s[0])]
    return returnCount        
    

if __name__ == "__main__":
    # print(searchNumerals("V"))
    print(convertToInt("MCMXCIV"))