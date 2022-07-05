class FileParser:
    """
        File Handlng operations are extended here
    """
    def isValidFile(self, FileName):

        isOk = False

        try:
            file = open(FileName, "r")
            isOk = True
            file.close()
        except:
            print("Exception while opening file")

        return  isOk

    def createIndexNameDic(self, FileName):

        IndexNameData = {}

        if self.isValidFile(FileName) == True:
            file = open(FileName, "r")

            for eachline in file.readlines():
                list = eachline.split(",")
                IndexNameData[int(list[0])] = list[1]

            file.close()

        return IndexNameData

    def parseCompanyData(self, FileName):

        CompanyData = {}

        if self.isValidFile(FileName) == True:
            file = open(FileName, "r")

            for eachline in file.readlines():
                list = eachline.split(",")
                KeyElement = list.pop(0).strip()

                if KeyElement.isdigit(): #non digit entries are junk or invalid
                    CompanyData[int(KeyElement)] =list

            file.close()

        return CompanyData

    def formateCompanyDataSheet(self, FileName):

        if self.isValidFile(FileName) == True:
            file = open(FileName, "r")

            output = []
            for eachline in file.readlines():

                list = eachline.split(",")
                if list.pop(0).strip().isdigit():
                    output.append(eachline)

            file.close()

            file = open(FileName, "w")
            file.writelines(output)

            file.close()

