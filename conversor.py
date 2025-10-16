import requests

#1 ---- Conversão de temperaturas ----
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    celsius = kelvin_to_celsius(kelvin)
    return celsius_to_fahrenheit(celsius)

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    return celsius_to_kelvin(celsius)
#1 -------------------------------------

#2 ---- Consultar temperatura da cidade ----
#Open Meteo

def get_cord(city):
    api_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    try:

        result = requests.get(api_url)

        if result.status_code == 200:
            dados = result.json()

            if "results" in dados:
                result = dados["results"][0]
                latitude = result["latitude"]
                longitude = result["longitude"]
                return latitude, longitude
            else:
                return None, None
    except requests.exceptions.RequestException as e:
        # Captura erros de conexão com a internet
        print(f"Erro de conexão: {e}")
        return None, None

def get_city_temp(latitude, longitude):

    api_url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    try:
        resposta = requests.get(api_url)
        if resposta.status_code == 200:
            dados = resposta.json()
            return dados["current_weather"]["temperature"]
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao buscar temperatura: {e}")
        return None

#2 end
#3 --- Menu ---
def menu():
  while True:
    print(f'\n--- Conversor e Consulta de Temperaturas ---')
    print('1 - Celsius -> Fahrenheit')
    print('2 - Fahrenheit -> Celsius')
    print('3 - Celsius -> Kelvin')
    print('4 - Kelvin -> Celsius')
    print('5 - Kelvin -> Fahrenheit')
    print('6 - Fahrenheit -> Kelvin')
    print('7 - Consultar temperatura de uma cidade')
    print('8 - Sair do Programa')

    choice = input('Escolha uma opção: ')

    if choice == '1':
        while True: # Loop adicionado para repetir o pedido
            try:
                c = float(input('Digite a temperatura em Celsius: '))
                print(f'Resultado: {celsius_to_fahrenheit(c):.2f} °F')
                break # Se deu certo, sai deste loop interno
            except ValueError:
                print('Erro: Por favor, insira um número válido. Tente novamente.')

    elif choice == '2':
        while True:
            try:
                f = float(input('Digite a temperatura em Fahrenheit: '))
                print(f'Resultado: {fahrenheit_to_celsius(f):.2f} °C')
                break
            except ValueError:
                print('Erro: Por favor, insira um número válido. Tente novamente.')

    elif choice == '3':
        while True:
            try:
                c = float(input('Digite a temperatura em Celsius: '))
                print(f'Resultado: {celsius_to_kelvin(c):.2f} K')
                break
            except ValueError:
                print('Erro: Por favor, insira um número válido. Tente novamente.')

    elif choice == '4':
        while True:
            try:
                k = float(input('Digite a temperatura em Kelvin: '))
                print(f'Resultado: {kelvin_to_celsius(k):.2f} °C')
                break
            except ValueError:
                print('Erro: Por favor, insira um número válido. Tente novamente.')

    elif choice == '5':
        # Aqui já apliquei as correções que sugeri anteriormente
        while True:
            try:
                k = float(input('Digite a temperatura em Kelvin: '))
                print(f'Resultado: {kelvin_to_fahrenheit(k):.2f} °F')
                break
            except ValueError:
                print('Erro: Por favor, insira um número válido. Tente novamente.')

    elif choice == '6':
        while True:
            try:
                f = float(input('Digite a temperatura em Fahrenheit: '))
                print(f'Resultado: {fahrenheit_to_kelvin(f):.2f} K')
                break
            except ValueError:
                print('Erro: Por favor, insira um número válido. Tente novamente.')

    elif choice == '7':
        city = input('Digite o nome da cidade: ')
        print('Buscando temperatura...')
        lat, lon = get_cord(city)
        if lat and lon:
            temperatura = get_city_temp(lat, lon)
            if temperatura is not None:
                print(f"A temperatura atual em {city.title()} é de {temperatura}°C.")
            else:
                print("Não foi possível obter a temperatura para esta cidade.")
        else:
            print(f"Não foi possível encontrar a cidade '{city}'. Tente novamente.")

    elif choice == '8':
        print('Obrigado por usar o programa. Até logo!')
        break

    else:
        print('Opção ínvalida. Escolha uma opção entre 1 e 8')
#3 end

#4 Start
if __name__ == "__main__":
    menu()
#4 end