def celcius_to_faherenheit(celcius):
    faherenheit=(celcius*9/5)+32
    return faherenheit
celcius=float(input("enter temperature in celcius: "))
faherenheit=celcius_to_faherenheit(celcius)
print(f"{celcius}C={faherenheit} F")