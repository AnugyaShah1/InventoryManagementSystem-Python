def Read_txt_file():
    with open('laptopfile.txt','r') as file:
        laptopID = 1
        myDict = {}
        for line in file:
            line = line.replace('\n','')
            myDict[laptopID] = (line.split(","))
            laptopID += 1
        return(myDict)

 


