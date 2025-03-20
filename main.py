import requests
from bs4 import BeautifulSoup
import re

base_url = "https://teknokentmaras.com/Kahramanmaras-Teknokent-Firma-Detay"
all_emails = set()


email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

for firma_id in range(1, 200):  
    url = f"{base_url}?firmaId={firma_id}"
    try:
        # Web sayfasını çek
        response = requests.get(url)
        response.raise_for_status()  # HTTP hatalarını kontrol et

        # Sayfa içeriğini parse et
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()

        # E-posta adreslerini bul
        emails = re.findall(email_pattern, text_content)
        all_emails.update(emails)
    except requests.exceptions.RequestException as e:
        print(f"Firma ID {firma_id} için hata oluştu: {e}")

with open("emails.txt", "w") as file:
    for email in all_emails:
        file.write(email + "\n")
print("emails.txt dosyasına yazıldı")