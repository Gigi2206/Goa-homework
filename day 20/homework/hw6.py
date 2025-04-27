#7) მომხმარებელს შემოაყვანინეთ წინადადება, შემდეგ for ციკლისა და პირობითი განცხადებების საშვალებით დაბეჭდეთ ჯერ ხმოვნების, შემდეგ კი თანხმოვნების რაოდენობა (ხმოვნებად ჩათვალეთ სიმბოლოები: a, e, i, o, u ხოლო სხვა ყველა თანხმოვნად)


sentence = input("გთხოვთ, შეიყვანოთ წინადადება: ").lower()
vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in sentence:
    if char in vowels:
        vowel_count += 1
    elif 'a' <= char <= 'z':  # შევამოწმოთ, რომ სიმბოლო არის ანბანის ასო
        consonant_count += 1

print("ხმოვნების რაოდენობა:", vowel_count)
print("თანხმოვნების რაოდენობა:", consonant_count)