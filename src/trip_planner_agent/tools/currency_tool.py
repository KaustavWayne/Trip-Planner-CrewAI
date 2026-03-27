import requests
import os

def convert_currency(amount, from_curr, to_curr):
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_curr}/{to_curr}/{amount}"

    response = requests.get(url)
    data = response.json()

    # 🔍 DEBUG PRINT (optional)
    print("API Response:", data)

    # ✅ Proper validation
    if data.get("result") != "success":
        raise ValueError(f"API Error: {data.get('error-type', 'Unknown error')}")

    if "conversion_result" not in data:
        raise ValueError("Conversion result missing in API response")

    return float(data["conversion_result"])