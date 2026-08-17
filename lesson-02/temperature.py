def check_temperature(temperature):
    if temperature >= 30:
        return "hot"
    elif temperature >= 20 and temperature <= 29:
        return "nice"
    elif temperature >= 10 and temperature <= 19:
        return "cold"
    else:
        return "very cold"

print(check_temperature(35))
print(check_temperature(25))
print(check_temperature(12))
print(check_temperature(2))