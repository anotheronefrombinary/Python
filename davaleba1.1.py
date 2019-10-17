#მომხმარებელს console დან შეამოატანინეთ სახელი, გვარი, დაბადების თარიღი. რის შემდეგაც :
#1) გამოიანგარიშეთ რამდენი წლის არი მომხმარებელი
#2) Advance გამოიანგარიშეთ რამდენი დღე არის დარჩენილი მოხმარებლის დაბადების დღემდე (ბიბლიოთეკის გამოყენება მისაღებია, თუ გაიაზრებთ რას #აკეთებთ copy/paste, მიუღებელია, ასევე ლექციაზე random ად აირჩევა სტუდენტი რომელიც თავის დაწერილ კოდს ახსნის)
#
#:> Solution: 
from datetime import date, datetime
name = input("Sheiyvanet tqveni saxeli: ")
surname = input("Sheiyvanet tqveni gvari: ")
dd = input("Sheiyvanet tqveni dabadebis ricxvi: ")
mm = input("Sheiyvanet tqveni dabadebis tve: ")
yy = input("Sheiyvanet tqveni dabadebis weli: ")
todaydd = datetime.now().day
todaymm = datetime.now().month
thisy = datetime.now().year
#გამოაქვს სახელი და გვარი
print("Tqveni saxeli da gvaria:", name, surname)
#თუ მომხმარებელს წინა თვეს ჰქონდა დაბადების დღე
if todaymm > int(mm):
  print("Da Tqven xart ", thisy-int(yy), "wlis")
#თუ მომხმარებელს ამ თვეში აქვს დაბადების დღე და უკვე ჰქონდა 
if (todaymm == int(mm) and (todaydd-int(dd))>0):
  print("Da Tqven xart", thisy-int(yy), "wlis")
#თუ მომხმარებელს ამ თვემდე ჯერ არ ჰქონია დაბადების დღე და მომავალ რომელიღაც თვეს აქვს
if todaymm < int(mm):
  print("Da Tqven xart", (thisy-int(yy))-1, "wlis")
#თუ მომხმარებელს ამ თვეში აქვს დაბადების დღე მაგრამ ჯერ არ ჰქონია
if (todaymm == int(mm) and (todaydd-int(dd))<0):
  print("Da Tqven xart", (thisy-int(yy))-1, "wlis")
#თუ მომხმარებელს დღეს აქვს დაბადების დღე
if (todaymm == int(mm) and todaydd == int(dd)):
  print("vax vax vax, aghmocnda rom dghes dabadebis dghe gaqvs, Leonidasi gilocavs dabadebis dghes! ", '\n' "Shen ukve", thisy-int(yy), "wlis xar, mrAVALs daeswari megobaro!", '\n', name, "Shens shemdeg dabadebis dghemde darchenilia 1 weli!")

dghes = date(datetime.now().year, datetime.now().month ,datetime.now().day)
var2 = date(datetime.now().year, int(mm), int(dd))

dabadebisdghemde = abs(dghes - var2)

if int(mm) < int(datetime.now().month):
  print("Tqvens dabadebis dghemde darcha", 365-dabadebisdghemde.days, "dghe")

if int(mm) == int(datetime.now().month) and int(dd) < int(datetime.now().day):
  print("Tqvens dabadebis dghemde darcha", 365-dabadebisdghemde.days, "dghe")

if int(mm) == int(datetime.now().month) and int(dd) > (datetime.now().day):
 print("Tqvens shemdeg dabadebis dghemde darcha", dabadebisdghemde.days, "dghe")

#PYTHONSQUAD
#წყარო:
#https://docs.python.org/3/library/datetime.html
#https://www.w3schools.com/python/python_conditions.asp
#კოდი თავისი წყაროებით აქ: https://AnotherOneFromBinary.com
print("\n","\n","See code and used sources here:", "\n","https://AnotherOneFromBinary.com")
print("#PYTHONSQUAD")