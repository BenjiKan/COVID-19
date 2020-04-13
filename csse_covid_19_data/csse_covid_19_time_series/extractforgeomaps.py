
# https://developers.google.com/chart/interactive/docs/gallery/geochart#displaying-proportional-markers
# http://www.covidcheatsheet.org/What_is_happening.html#history_block

import csv

shortData = [['latitude', 'longitude', 'city', 'state', 'country', 'cases']]
visualizationData = [['latitude', 'longitude', 'city', 'state', 'country', 'cases']]

with open('time_series_covid19_confirmed_US.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count != 0): #if not header row,
            visualizationData.append([float(row[8]), float(row[9]), row[5], row[6], row[7], row[len(row)-1]])
            if (line_count <= 25): # additionally, append to shorter data array
                shortData.append([float(row[8]), float(row[9]), row[5], row[6], row[7], row[len(row)-1]])
        line_count += 1
        
print(line_count)
print(shortData)

with open("shortdata.txt", "w") as f:
    for row in shortData:
        f.write("%s\n" % row)

f.close()

with open("fulldata.txt", "w") as f:
    for row in visualizationData:
        f.write("%s\n" % row)

f.close()




