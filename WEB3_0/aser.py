import requests

url = 'http://127.0.0.1:8000/transfer/'  # Замените 'your-api-url' на URL вашего API

data = {
    'source_inn': '555555555555',  # ИНН отправителя (строка)
    'target_inn': '566780023004',  # ИНН получателя (строка)
    'amount': 500.00,           # Сумма перевода (число)
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("Перевод выполнен успешно.")
else:
    print("Ошибка при выполнении перевода:", response.text)
    print("hello matherfucker")