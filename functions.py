
def power(value):
    return value**2

def how_long(value=None):
    if (value != None):
        return len(value)
    else:
        return "No length"

def converter(origin_unit, units="m", coefficient=0.348):
    result = (origin_unit * coefficient)
    return f"{result} {units}"

def cels_to_fah(celsius):
    return (celsius * 9/5) + 32

print("10 degrees celsius is ", cels_to_fah(10), "Fahrenheit")
print(converter(4, "km", 0.6))
