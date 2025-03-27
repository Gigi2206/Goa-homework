"""2) განმარტეთ control flow, ჩამოწერეთ მისი შემადგენელი ტექნიკები, აღწერეთ თითოეული"""

# 1. თანმიმდევრობა (Sequence)
# ბრძანებები სრულდება ზემოდან ქვემოთ, თანმიმდევრობით.

print("პირველი ბრძანება")
x = 5
y = x + 10
print("მეორე ბრძანება:", y)
print("მესამე ბრძანება")

# 2. არჩევანი (Selection/Branching)

# 2.1. if განცხადება
a = 10
if a > 5:
    print("a მეტია 5-ზე")

# 2.2. if-else განცხადება
b = 3
if b > 5:
    print("b მეტია 5-ზე")
else:
    print("b არ არის მეტი 5-ზე")

# 2.3. if-elif-else განცხადება
c = 7
if c > 10:
    print("c მეტია 10-ზე")
elif c > 5:
    print("c მეტია 5-ზე, მაგრამ არა 10-ზე")
else:
    print("c არ არის მეტი 5-ზე")

# 3. გამეორება (Iteration/Looping)

# 3.1. for ციკლი
# გამოიყენება კოლექციებზე (მაგ., სია, ტუპლი, სტრიქონი) გადასალაგებლად
fruits = ["ვაშლი", "ბანანი", "ფორთოხალი"]
for fruit in fruits:
    print(fruit)

# გამოიყენება დიაპაზონში გამეორებისთვის
for i in range(5):  # გაიმეორებს 0-დან 4-მდე
    print(f"რიცხვი: {i}")

# 3.2. while ციკლი
count = 0
while count < 5:
    print(f"Count არის: {count}")
    count += 1

# 4. გადახტომა (Jumping)

# 4.1. break განცხადება
for i in range(10):
    if i == 5:
        break  # ციკლიდან გამოსვლა, როდესაც i არის 5
    print(f"i არის: {i}")

# 4.2. continue განცხადება
for i in range(10):
    if i % 2 == 0:
        continue  # გადადის შემდეგ იტერაციაზე, თუ i ლუწია
    print(f"კენტი რიცხვი: {i}")

# 4.3. return განცხადება (ფუნქციებში)
def add_numbers(x, y):
    return x + y

sum_result = add_numbers(3, 7)
print(f"ჯამი არის: {sum_result}")















