import os

class WriteFile:

    def __init__(self, filename):
        self.__file = open(filename,'w')
        self.__file.write("terminal;Status")
        self.__file.write('\n')

    def writer(self,row):
        self.__file.write(row)
        self.__file.write('\n')

    def writerRows(self,rows):
        self.__file.writelines(rows)        
    
    def close(self):
        self.__file.close()


if __name__ == '__main__':
    filename = 'C:/DADOS/Test_File.csv'
    w = WriteFile(filename)
    lst = []
    lst.append("35987221451;invalid")
    lst.append("51984771376;valid")
    lst.append("51984055999;invalid")
    lst.append("32988890822;valid")
   
    for each_Value in lst:
        w.writer(each_Value)
    #w.writerRows(csvData)
    w.close()
    print(filename)
