from statistics import mean
import csv


inpChar = input('Enter char from A-Z: ')
stockOutputField = ['Symbol','Open','High','Low','LTP','Chng','% Chng']
fileName = 'lab_11_data.csv'
avgoutFN = 'avg_output.txt'
stockoutFN = 'stock_output.txt'


#Solution 1

lambdaDropCol = lambda data: data[0: 7]

# Solution 2

lfun = lambda data: float(data[6]) > -3
lopen = lambda data: float(data[1].replace(',', ''))
llow = lambda data: float(data[3].replace(',', ''))
lhigh = lambda data: float(data[2].replace(',', ''))

#Solution 4

lschar = lambda data: data[0][0] == inpChar
fields = []
tdropcol = []
with open(fileName, 'r') as f:
    reader = csv.reader(f)
    fields = next(reader)
    for row in reader:
        tdropcol.append(lambdaDropCol(row))

tdropnewrows = list(filter(lfun, tdropcol))

openVal = list(map(lopen, tdropnewrows))
lowvalue = list(map(llow, tdropnewrows))
highvalue = list(map(lhigh, tdropnewrows))


avgOpen=mean(openVal)
avgLow =mean(lowvalue)
avgHigh=mean(highvalue)


filterstartchar = list(filter(lschar, tdropnewrows))


#Solution 3

with open(avgoutFN, 'w', encoding = 'utf8') as csvFile:
    openAvg = str(avgOpen) + '\n'
    lowAvg = str(avgLow) + '\n'
    highAvg = str(avgHigh) + '\n'
    
    csvFile.write(openAvg)
    csvFile.write(highAvg)
    csvFile.write(lowAvg)


# Solution 5

with open(stockoutFN, 'w', newline = '', encoding = 'utf8') as csvFile:
    for row in filterstartchar:
        s = ' '.join(row)
        s =s+ '\n'
        csvFile.write(s)