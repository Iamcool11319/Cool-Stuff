print("BMI Calculator")
imperial_height = input("Height(in): ")
imperial_weight = input("Weight(lbs): ")
converted_imperial_height = float(imperial_height)
converted_imperial_weight = float(imperial_weight)
metric_height = converted_imperial_height * 0.0254
metric_weight = converted_imperial_weight * 0.453592
print(metric_weight / metric_height ** 2)
