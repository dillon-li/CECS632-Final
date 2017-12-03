import csv
import sys

#def animeTest(fullList):
    # Group 1

#def main():
filename = sys.argv[1]
# Generate the dictionary to work with
with open(filename, 'rU') as f:
    reader = csv.reader(f)
    headers = reader.next()
    fullList = {}
    for row in reader:
        attCount = 1
        animeID = row.pop(0)
        newDict = {}
        for item in row:
            #print headers[attCount]
            newDict[headers[attCount]] = item
            attCount = attCount + 1
        fullList[animeID] = newDict
    print(fullList['5114']['name'])
