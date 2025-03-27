"""4) თქვენ მიერ დაწერილი კოდებიდან აარჩიეთ ერთერთი და შექმენით მისი flowchart"""

def is_positive(number):
  
  """ეს ფუნქცია ამოწმებს, არის თუ არა რიცხვი დადებითი."""
  
  if number > 0:
    return True
  else:
    return False

# მაგალითი გამოყენებისთვის:
num1 = 5
print(f"{num1} არის დადებითი: {is_positive(num1)}")

num2 = -2
print(f"{num2} არის დადებითი: {is_positive(num2)}")

num3 = 0
print(f"{num3} არის დადებითი: {is_positive(num3)}")












