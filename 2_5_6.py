file = open('climate.csv', 'r')

climate = file.readlines()

print(climate)



newList = []
for line in climate:
   if line[-1] == '\n':
       newList.append(line[:-1])
       newList.append(line.strip())
   else:
       newList.append(line)

print(newList)