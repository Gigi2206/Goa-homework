"""6) Bonus დავალება
შექმენით პროგრამა, რომელიც განსაზღვრავს productive ცვლადის მნიშვნელობას შემდეგი პირობების მიხედვით:
read_pages ცვლადში ინახება წაკითხული გვერდების რაოდენობა (მთლიანი რიცხვი).
free_time ცვლადში ინახება boolean მნიშვნელობა (True/False), რომელიც გვიჩვენებს, ჰქონდა თუ არა თავისუფალი დრო.
productive ცვლადი იქნება ჭეშმარიტი (True), თუ მოსწავლემ წაიკითხა მინიმუმ 20 გვერდი და თავისუფალი დრო ჰქონდა.
"""
read_pages = int(input("რამდენი გვერდი წაიკითხე: "))
free_time = bool(input("გქონდა თავისუფალი დრო? (true/false): "))
productive = read_pages >= 20 and free_time
print(productive)