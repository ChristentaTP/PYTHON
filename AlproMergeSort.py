# Christenta Tirta Pradieva (21120122140137)
# Lucky Barga Aretama (21120122140138)
# Pseudocode MergeSorting

list1 = [1, 8, 5 ,0, 7, 3]
list2 = [99, 23, 2, 44, 98, 6 ]
list3 = list1 + list2


for i in range(len(list2)):
      for x in range(len(list2)):
         if list1[i] < list1[x]:
             decoy = list1[x]
             list1[x] = list1[i]
             list1[i] = decoy
        
         elif(list2[i] < list2[x]):
            decoy = list2[x]
            list2[x] = list2[i]
            list2[i] = decoy

for l in range(len(list3)):
    for g in range(len(list3)):
        if(list3[l] < list3[g]):
            decoy = list3[g]
            list3[g] = list3[l]
            list3[l] = decoy

print("list 1 =%s" %list1)
print("list 2 =%s" %list2)
print(list3)
