with open("1.txt") as file:
    arr1 = [int(row.strip()) for row in file]
    
with open("2.txt") as file:
    arr2 = [int(row.strip()) for row in file]
    
set1 = set(arr1);
set2 = set(arr2);

print(set1);
print(set2);