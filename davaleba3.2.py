a = input("Sheiyvanet nebismieri texturi mnishvnelobebi, gamoyavit mdzimit: ").split(",")
#წინაპირობა
if len(a) % 2 == 1:
  shua = len(a)/2
  shuaelement = a[int(shua)]
#თუ მასივში კენტი რაოდენობის ელემენტებია და შუა ელემენტიც კენტია
if len(a) % 2 == 1 and len(shuaelement) % 2 == 1:
  shuaelementshua =  shuaelement[int(len(shuaelement)/2)]
  print("Masivis shua elementia: ", a[int(shua)])
  print("Da misi shua simboloa: ", shuaelementshua)
#თუ მასივში კენტი რაოდენობის ელემენტებია და შუა ელემენტი ლუწია
if len(a) % 2 == 1 and len(shuaelement) % 2 == 0:
  x1 = len(shuaelement)/2-1
  x2 = len(shuaelement)/2+1
  shuaelementshua = shuaelement[int(x1):int(x2)]
  print("Masivis shua elementia: ", a[int(shua)])
  print("Da misi shua simboloa: ", shuaelementshua)
### START OF: ორ წევრიანი მასივი, რომელთაგან ერთი კენტია ერთი ლუწი.
#: პირველი წევრი კენტია მეორე ლუწი:
if len(a) == 2 and len(a[0]) % 2 == 1 and len(a[1]) % 2 == 0:
  z1 = len(a[0])/2
  z2 = len(a[0])/2+1
  z3 = len(a[1])/2-1
  z4 = len(a[1])/2+1
  print("Masivis elementebis shua simboloebia: ", a[0][int(z1):int(z2)], a[1][int(z3):int(z4)])
#:>Reverse:
#: პირველი წევრი ლუწია მეორე კენტი:
if len(a) == 2 and len(a[1]) % 2  == 1 and len(a[0]) % 2 == 0:
  z1 = len(a[1])/2
  z2 = len(a[1])/2+1
  z3 = len(a[0])/2-1
  z4 = len(a[0])/2+1
  print("Masivis elementebis shua simboloebia: ", a[0][int(z3):int(z4)], a[1][int(z1):int(z2)])
###: END OF: ორ წევრიანი მასივი.
  
###: START OF: თუ მასივში ლუწი რაოდენობის ელემენტია, გარდა ორისა. (4, 6, 8..)

#თუ ლუწი რაოდენობის ელემენტებიანი მასივის შუა ორი წევრიდან პირველი კენტია და მეორე ლუწი:>
mida = a[int(len(a)/2-1)]
midb = a[int(len(a)/2)]
if len(a) % 2 == 0 and len(mida) % 2 == 1 and len(midb) % 2 == 0:
  print("Shua wevrebia: ", mida, midb)
  a1 = len(mida)/2 #kentishua
  a2 = len(midb)/2-1 #luwishua1
  a3 = len(midb)/2+1 #luwishua2
  print("Shua wevrebis shua simboloebia: ", mida[int(a1)], midb[int(a2):int(a3)])

#თუ ლუწი რაოდენობის ელემენტებიანი მასივის შუა ორი წევრიდან პირველი ლუწია და მეორე კენტი:>
if len(a) % 2 == 0 and len(mida) % 2 == 0 and len(midb) % 2 == 1:
  print("Shua wevrebia: ", mida, midb)
  a1 = len(midb)/2 #kentishua
  a2 = len(mida)/2-1 #luwishua1
  a3 = len(mida)/2+1 #luwishua2
  print("Shua wevrebis shua simboloebia: ", mida[int(a2):int(a3)], midb[int(a1)])
#თუ ლუწი რაოდენობის ელემენტებიანი მასივის შუა ორი წევრიდან ორივე ლუწია:
if len(a) % 2 == 0 and len(mida) % 2 == 0 and len(midb) % 2 == 0:
  print("Shua wevrebia: ", mida, midb)
  a1 = len(mida)/2-1
  a2 = len(midb)/2+1
  print("Shua wevrebis shua simboloebia:", mida[int(a1):int(a2)], midb[int(a1):int(a2)])
#თუ ლუწი რაოდენობის ელემენტებიანი მასივის შუა ორი წევრიდან ორივე კენტია:
if len(a) % 2 == 0 and len(mida) % 2 == 1 and len(midb) % 2 == 1:
  print("Shua wevrebia: ", mida, midb)
  a1 = len(mida)/2
  a2 = len(midb)/2
  print("Shua wevrebis shua elementebia: ", mida[int(a1)], midb[int(a2)])
#GitHub: https://github.com/anotheronefrombinary/Python/blob/master/davaleba3.2.py