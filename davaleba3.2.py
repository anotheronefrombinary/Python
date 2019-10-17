#ექმენით dictionary სადაც key:value იქნება თქვენი სახელი და ასაკი(KEY იქნება თქვენი სახელი, VALUE იქნება თქვენი ასაკი)
#დაბეჭდეთ რამდენი key:value წყვილისგან შედგება dictionary.
#შექმენით tuple, რომელშიც იქნება შემდეგი სიტყვები : guido, tim
#ამის შემდეგ მომხარებელს მიეცით საშუალება შეიყვანონ სახელი და ასაკი.
#თუკი სახელი არის tuple-ში, მაშინ მომხარებლის მიერ შეყვანილი სახელი და ასაკი დაამატეთ თავდაპირველად შექმნილ dictionary-ში.
#ხელახლა დაბეჭდეთ რამდენი key:value წყვილისგან შედგება dictionary.
#:> Solution:
bibl = {"levan":18}
tpl = ("guido", "tim")
print(len(bibl))
name = input("Sheiyvanet tqveni saxeli: ")
age = input("Sheiyvanet tqveni asaki: ")
if name == tpl[0] or tpl[1]:
	bibl.[name] = age
print(len(bibl))