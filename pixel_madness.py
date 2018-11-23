result=""

for line in open("text.txt"):
  tableau = line.split("+")
  for j in range(len(tableau)):
    result+= tableau[j][0] * int(tableau[j][2:])
  result+="\n"

result = result.replace("0"," ")
result = result.replace("1","█")
print(result)
