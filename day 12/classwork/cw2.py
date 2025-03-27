"""2) სამივე ლოგიკურ ოპერატორზე: not, or, and: ჩამოწერეთ ყველა შესაძლო ვარიანტი და დაბეჭდეთ შედეგი გვერდზე კომენტარის საშვალებით მიწუერეთ შედეგი """

a = True
b = True
print(a and b, " # True")
print(a or b, "  # True")
print(not a,   "  # False")
print(not b,   "  # False")

a = True
b = False
print(a and b, " # False")
print(a or b, "  # True")
print(not a,   "  # False")
print(not b,   "  # True")

a = False
b = True
print(a and b, " # False")
print(a or b, "  # True")
print(not a,   "  # True")
print(not b,   "  # False")

a = False
b = False
print(a and b, " # False")
print(a or b, "  # False")
print(not a,   "  # True")
print(not b,   "  # True")



