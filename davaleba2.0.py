#მოცემულია სია იგივე მასივი
#
#sia = ["abc", "d", "efghi", "j", "klmnop", "qr","st","uv","wxyz"]
#
#დავალება:
#
#სიის იგივე მასივის გამოყენებით ააწყვეთ თქვენი სახელი და გვარი,
#რის შემდეგაც დაბეჭდეთ მხოლოდ თქვენი სახელის ბოლო ორი ხოლო თქვენი
#გვარის პირველი სამი ასო ერთად.
#ასევე შექმენით 3 ცვლადი რომლიდანაც 2 ს კონსოლიდან მიანიჭებთ
#მნიშვნელობას შედეგად სამივეს დაამატებთ sia ში append ის დახმარებით
#და დაბეჭდავთ.
#
#hint:
#sia[0][0] = "a"
#:> Solution: 
sia = ["abc", "d", "efghi", "j", "klmnop", "qr","st","uv","wxyz"]
saxeli = (sia[4][1]+sia[2][0]+sia[7][1]+sia[0][0]+sia[4][3])
gvari = (sia[0][0]+sia[7][1]+sia[0][0]+sia[4][1]+sia[2][4]+sia[0][0]+sia[4][3]+sia[2][4])
boloori_saxeli = len(saxeli)-2
print(saxeli, gvari)
print(saxeli[boloori_saxeli:len(saxeli)]+gvari[0:3])
var1 = input("Himalai tu ushba? ")
var2 = input("boy boy boy cis qvesh dgaxar? ")
var3 = "flugengenecholen"
sia.append(var1)
sia.append(var2)
sia.append(var3)
print(sia[len(sia)-3:len(sia)])


