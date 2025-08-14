def CelciusToFahrenheit():
    print("Algoritimo de mudança de Celsius para farenheit")
    try:
        celcius = float(input("Informe uma temperatura em Celsius: "))
        convert = (celcius * (9/5)) + 32
        print(f"{celcius} graus em Fahrenheit sera de {convert} graus")
    except ValueError:
        print("Valores somente numericos serão aceitos")
    
if __name__ == "__main__":
    CelciusToFahrenheit()
    