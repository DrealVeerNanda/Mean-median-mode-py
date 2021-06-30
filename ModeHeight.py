import csv
from collections import Counter
with open("HeightWeight.csv", newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
#to remove the list of the titles using pop
file_data.pop(0)
#sorting the data for height
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))

#mode
data = Counter(new_data)
#creating range
mode_data_for_range = {"50-60": 0, "60-70": 0, "70-80": 0}

#if for each range
for height, occurrence in data.items():
    if 50 < float(height) < 60: 
        mode_data_for_range["50-60"] += occurrence #increasing occurrence by 1
    elif 60 < float(height) < 70: 
        mode_data_for_range["60-70"] += occurrence #increasing occurrence by 1
    elif 70 < float(height) < 80:
        mode_data_for_range["70-80"] += occurrence #increasing occurrence by 1


mode_range, mode_occurrence = 0,0
for range, occurrence in mode_data_for_range.items():
    if(occurrence > mode_occurrence): 
        mode_range, mode_occurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurrence


mode = float((mode_range[0] + mode_range[1]) / 2) 
print(f"Mode is -> {mode:2f}")       