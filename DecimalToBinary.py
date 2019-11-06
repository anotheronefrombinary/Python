#Decimal to binary converter by leonidas  
a = input("Sheiyvanet ricxvi romlis gadayvanac gindat binaryshi: ")
numtobin = []
b = a
num = ""
#START OF CONVERTER
while int(a) > 0:
  if int(a) % 2 == 1:
    numtobin.insert(0, int(a)%2)
    a = int(int(a)/2)
  if int(a) % 2 == 0:
    numtobin.insert(0, int(a)%2)
    a = int(int(a)/2)
numtobin.remove(0)
index = 0
for i in numtobin:
  num += str(i)
num = int(num)
#END OF CONVERTER
print("{} binaryshi aris: ".format(b), num)
#AnotherOneFromBinary
#Git: https://github.com/anotheronefrombinary