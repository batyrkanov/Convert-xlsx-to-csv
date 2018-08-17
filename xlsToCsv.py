def generateRows(i):
    import csv
    with open('csv_file.csv', 'w') as csvfile:
        fieldnames = ['Код', 'Наименование на русском', 'Наименование на кыргызском']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,quoting=csv.QUOTE_NONE, delimiter=";")

        writer.writeheader()
        while i<100000:
            writer.writerow({'Код': i, 'Наименование на русском': "A"+str(i), 'Наименование на кыргызском': "B"+str(i)})
            i+=1
def deleteEmptyRows():
    import csv
    import os

    with open('csv_file.csv') as input, open('out.csv', 'w', newline='') as output:
        writer = csv.writer(output)
        for row in csv.reader(input):
            if any(field.strip() for field in row):
                writer.writerow(row)
    os.remove('csv_file.csv')

import csv
i = 0
generateRows(i)
deleteEmptyRows()
