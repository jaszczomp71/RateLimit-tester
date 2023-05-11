import requests
import time

# Ustawienia testu
url = 'https://xxxx.xxx.xxxx.xx'  # adres URL endpoint
liczba_zadan = 30  # liczba zadań do wykonania
przerwa = 0.5  # czas oczekiwania między zadaniami w sekundach

for i in range(liczba_zadan):
    
    response = requests.get(url)
    
    if response.status_code == 405:
        print(f'Zadanie {i+1}: Otrzymano kod 405 (błąd danych logowania)')
    
    elif response.status_code == 503:
        print(f'Zadanie: {i+1}: Otrzymano kod 503 (przekroczony limit zapytani/1min.)')
    
    else:    
         print(f'Zadanie {i+1}: Otrzymano kod {response.status_code}')
    time.sleep(przerwa)
