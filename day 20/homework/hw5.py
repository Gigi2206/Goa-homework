#6) მომხმარებელმა უნდა შეიყვანოს რიცხვები, სანამ -1-ს არ შეიყვანს. საბოლოოდ გამოიანგარიშოს შეყვანილი რიცხვების საშუალო


total_sum = 0
count = 0

while True:
    user_input = input("გთხოვთ, შეიყვანოთ რიცხვი (-1 შესაჩერებლად): ")
    number = int(user_input)
    if number == -1:
        break
    total_sum += number
    count += 1

if count > 0:
    average = total_sum / count
    print("შეყვანილი რიცხვების საშუალოა:", average)
else:
    print("არცერთი რიცხვი არ შეყვანილა (გარდა -1-ისა).")