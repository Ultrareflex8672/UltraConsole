from application.ultraconsole import UltraConsole as UC


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit_from, unit_to):
    if unit_from == unit_to:
        return value  # Aynı birimde ise değiştirme

    if unit_from == "c" and unit_to == "f":
        return celsius_to_fahrenheit(value)
    elif unit_from == "c" and unit_to == "k":
        return celsius_to_kelvin(value)
    elif unit_from == "f" and unit_to == "c":
        return fahrenheit_to_celsius(value)
    elif unit_from == "f" and unit_to == "k":
        return fahrenheit_to_kelvin(value)
    elif unit_from == "k" and unit_to == "c":
        return kelvin_to_celsius(value)
    elif unit_from == "k" and unit_to == "c":
        return kelvin_to_fahrenheit(value)
    else:
        return None  # Geçersiz giriş

# Kullanıcıdan giriş al
# value = float(input("Dönüştürmek istediğiniz sıcaklık değerini girin: "))
value = int(UC.create_frame("Sıcaklık Birimi Dönüşümü", "Dönüştürmek istediğiniz sıcaklık değerini girin: ",""))
# unit_from = input("Girdiğiniz sıcaklığın birimi (C, F, K): ").upper()
unit_from = UC.create_frame("Sıcaklık Birimi Dönüşümü", "Girdiğiniz sıcaklığın birimi (C, F, K): ","")
# unit_to = input("Dönüştürmek istediğiniz birim (C, F, K): ").upper()
unit_to = UC.create_frame("Sıcaklık Birimi Dönüşümü", "Dönüştürmek istediğiniz birim (C, F, K): ","")

def sicaklikcevirme(**kwargs):
    # Dönüştürme işlemi
    result = convert_temperature(value, unit_from.lower(), unit_to.lower())

    if result is not None:
        # print(f"{value}°{unit_from} = {result:.2f}°{unit_to}")
        UC.create_frame("Sıcaklık Birimi Dönüşümü", f"{value}°{unit_from.upper()} = {result:.2f}°{unit_to.upper()}", "info")
    else:
        # print("Geçersiz giriş! Lütfen C, F veya K birimlerinden birini girin.")
        UC.create_frame("Sıcaklık Birimi Dönüşümü Hatası", "Geçersiz giriş! Lütfen C, F veya K birimlerinden birini girin.", "info")

