sum = 0
for counter in range(12): #(1, 13) (0, 12)
    Age = int(input('Enter Age: '))
    sum += Age

Average = sum / counter
print("Age average: ",Average)
