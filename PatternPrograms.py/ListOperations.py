def listoperation(sampleList):
    a=0
    print("sampleList",sampleList)
    sampleList.append(10) #Add a number to the list.
    print("Addition", sampleList)
    print("Remove",sampleList.pop()) #Remove a number from the list.
    for x in sampleList: #Sum
        a+=x
    print("Sum",a) 
    average = a//len(sampleList) #Average
    print("average",average)
    maximumValue = max(sampleList) #maximum
    print("maximumValue", maximumValue)
listoperation([1,2,3,4,5])


