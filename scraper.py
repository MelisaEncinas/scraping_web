import requests
from bs4 import BeautifulSoup

# URL de tu blog local
url = 'http://127.0.0.1:5000/'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    titles = soup.find_all('h2')
    
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title.get_text()}")
else:
    print(f"Error al acceder a la página: {response.status_code}")
