#3) მომხმარებელს შემოატანინეთ რიცხვი 0-იდან 4-მდე და შეინახეთ ის "user_choice"-ის ცვლადში, შემდეგ ბოსტნეულსი სიიდან დაუბეჭდეთ ის ელემენტი რომელიც მომხმარებელმა აირჩია, ესეიგი იმ user_choice ინდექსზე მყოფი ელემენტი სიაში

# შევქმნათ ბოსტნეულის სია
ბოსტნეული = ["კარტოფილი", "სტაფილო", "კომბოსტო", "პომიდორი", "ბროკოლი"]

# მომხმარებელს შემოვატანინოთ რიცხვი 0-დან 4-მდე
while True:
    try:
        user_choice_str = input("შეიყვანეთ რიცხვი 0-დან 4-მდე: ")
        user_choice = int(user_choice_str)
        if 0 <= user_choice <= 4:
            break
        else:
            print("გთხოვთ, შეიყვანოთ რიცხვი 0-დან 4-მდე.")
    except ValueError:
        print("გთხოვთ, შეიყვანოთ მთელი რიცხვი.")

# დავბეჭდოთ არჩეული ელემენტი სიიდან
print("თქვენ აირჩიეთ:", ბოსტნეული[user_choice])