def convertTemperature(self, celsius):
    kelvin=celsius + 273.15
    fahrenhit = celsius * 1.80 +32
    return [kelvin,fahrenhit]
y=convertTemperature(1,25)
print(y)