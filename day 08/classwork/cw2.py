"""2) მომხმარებელს input-ის საშვალებით შემოტანინეთ ორი რიცხვი number1 და
 number2 შემდეგ კი დაბეჭდეთ მათი ჯამი. ასევე შექმენით level-ის ცვლადი რომელშიც მომხამრებელს შემოაყვანინებთ
   მათ ამჟამინდელ level-ს, შეეცადეთ level-ის მნიშვნელობას დაუმატოთ ერთი 
და ისე დაბეჭდოთ. მიღებული შედეგებით გამოიტანეთ დასკვნა და დაწერეთ კომენტარებით"""

number1 = input("choose number1: ") #შევქმენი ცვლადი number1.
number2 = input("choose number2: ") #შევქმენი ცვლადი number2.

print( number1 + number2 ) #გამოიტანე ეკრანზე მათი ჯამი.

current_level = int(input("write current level: ")) #ვაქციე ინტეჯერად ინფუთი.

print(current_level + 1)  #დავპრინტე.

