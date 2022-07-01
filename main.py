import requests
from bs4 import BeautifulSoup


headers = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

def get_location(url):
  response = requests.get(url=url, headers=headers)
  soup = BeautifulSoup(response.text, 'lxml')

  ip = soup.find('div', class_='ip').text.strip()
  print(ip)

def main():
  get_location(url='https://2ip.ru')


if __name__ == '__main__':
  main()
