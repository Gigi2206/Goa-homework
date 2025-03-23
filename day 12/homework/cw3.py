# ცვლადები
read_pages = 25  # წაკითხული გვერდების რაოდენობა
free_time = True  # ჰქონდა თუ არა თავისუფალი დრო

# პროდუქტიულობის განსაზღვრა
productive = read_pages >= 20 and free_time

# შედეგის გამოტანა
print(f"წაკითხული გვერდები: {read_pages}")
print(f"თავისუფალი დრო: {free_time}")
print(f"პროდუქტიულია: {productive}")