# ცვლადები ლოგიკური და შედარების ოპერაციების შედეგების შესანახად

temperature = 25
is_cloudy = False
is_raining = True

result1 = temperature > 30 and not is_cloudy  # False (temperature არ არის 30-ზე მეტი)
result2 = temperature < 30 or is_raining  # True (temperature ნაკლებია 30-ზე)
result3 = (temperature > 20) and (not is_raining or is_cloudy) # True (temperature მეტია 20-ზე და is_raining არ არის true)
result4 = not is_cloudy and is_raining or temperature == 25 # True (is_cloudy არ არის true, is_raining არის true ან temperature უდრის 25-ს)
result5 = (temperature > 30 or is_raining) and not (temperature < 20) # False (temperature არ არის 30-ზე მეტი და is_raining არის true მაგრამ temperature არ არის 20-ზე ნაკლები)

# შედეგების გამოტანა
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)