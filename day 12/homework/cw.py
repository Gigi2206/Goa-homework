# > (მეტი)
print(10 > 5)  # True
print(3 > 7)   # False
print("apple" > "banana")  # False (ლექსიკოგრაფიული შედარება)
print(10.5 > 10)  # True
print(-1 > -5)  # True

# >= (მეტი ან ტოლი)
print(10 >= 10)  # True
print(15 >= 10)  # True
print(5 >= 10)   # False
print("hello" >= "hello")  # True
print(20.5 >= 20)  # True

# < (ნაკლები)
print(5 < 10)  # True
print(10 < 5)  # False
print("banana" < "apple")  # False (ლექსიკოგრაფიული შედარება)
print(10 < 10.5)  # True
print(-5 < -1)  # True

# <= (ნაკლები ან ტოლი)
print(10 <= 10)  # True
print(5 <= 10)  # True
print(10 <= 5)  # False
print("hello" <= "hello")  # True
print(20 <= 20.5)  # True

# == (ტოლი)
print(10 == 10)  # True
print("hello" == "hello")  # True
print(10 == "10")  # False (Python არ ახორციელებს ავტომატურ კონვერტაციას)
print(True == 1)  # True (Boolean-ები რიცხვებად ითვლება)
print(None == None) #True

# != (არ არის ტოლი)
print(10 != 5)  # True
print("hello" != "world")  # True
print(10 != "10")  # True (Python არ ახორციელებს ავტომატურ კონვერტაციას)
print(True != 0)  # True (Boolean-ები რიცხვებად ითვლება)
print(None != 0) # True

