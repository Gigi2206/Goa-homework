#5) მომხმარებელს 3 მცდელობა აქვს სწორი PIN კოდის შეყვანისთვის. თუ შეიყვანს სწორად, დაიბეჭდება "Access Granted", სხვა შემთხვევაში "Access Denied" გამოიყენეთ პირობითი განცხადებები.


correct_pin = "1234"  # ჩაანაცვლეთ თქვენი რეალური PIN კოდით
attempts_left = 3

while attempts_left > 0:
    user_pin = input(f"გთხოვთ, შეიყვანოთ PIN კოდი (დარჩენილი მცდელობა: {attempts_left}): ")
    if user_pin == correct_pin:
        print("Access Granted")
        break  # სწორი PIN კოდის შეყვანის შემდეგ ციკლი წყდება
    else:
        attempts_left -= 1
        print("Access Denied")

if attempts_left == 0:
    print("მცდელობები ამოიწურა.")