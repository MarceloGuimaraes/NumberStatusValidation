import csv,os

class ReadFile:
    def __init__(self, filename,delimiter):
        self.file = open(filename)
        self.delimiter = delimiter

    def read(self):
        reader = csv.reader(self.file, delimiter=self.delimiter)
        rowCount = 0
        arrayPhones = []
        next(reader, None) 
        for row in reader:
            arrayPhones.append(row[2])
            if rowCount == 3:
                arrayPhones.clear()
                rowCount = 0
            rowCount = rowCount +1  

    def close(self):
        self.file.close()

if __name__ == '__main__':
    filename = 'C:/file.csv'
    r = ReadFile(filename,';')
    r.read()
    r.close()