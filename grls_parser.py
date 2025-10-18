import requests
import json
import time

url = "https://grls.rosminzdrav.ru/GrlsApi/GrlsList"

headers = {
    "User-Agent": "LekSpravka Bot (contact: your.email@example.com)",
    "Content-Type": "application/json"
}

payload = {
    "Page": 1,
    "Size": 50,
    "Filter": {
        "Mnn": "",
        "TradeName": "",
        "Producer": ""
    }
}

print("Запрашиваем данные из ГРЛС...")
try:
    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()
    print(f"✅ Получено {len(data['Data'])} препаратов")

    with open("drugs.json", "w", encoding="utf-8") as f:
        json.dump(data["Data"], f, ensure_ascii=False, indent=2)

    print("💾 Данные сохранены в drugs.json")
except Exception as e:
    print("❌ Ошибка:", e)