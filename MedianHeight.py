import csv

with open("HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
#to remove the list of the titles using pop
file_data.pop(0)
#sorting the data for height
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1] # this specifies that it is in column 1 which is the height!
    new_data.append(float(n_num))

#orders from least to greatest
n = len(new_data)
new_data.sort()
# // is floor division to round it to the nearest whole #
if n % 2 == 0:
    median1 = float(new_data[n//2]) 
    median2 = float(new_data[n//2-1])
    median = (median1 + median2)/2
else: 
    median = new_data[n//2]
    print(n)
print("median is "+ str(median))
