import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_private_results(query):
    headers = {
        "User-Agent": "",
        "Referer": "",
        "DNT": "1"
    }

    url = f"https://html.duckduckgo.com/html/?q={query}"
    try:
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        results = []
        for a in soup.find_all('a', class_='result__a'):
            title = a.get_text()
            href = a['href']

            # Decode and clean redirect URLs
            if "duckduckgo.com/l/uddg=" in href:
                parsed = urllib.parse.urlparse(href)
                params = urllib.parse.parse_qs(parsed.query)
                real_url = params.get('uddg', [href])[0]
                clean_link = urllib.parse.unquote(real_url)
            else:
                clean_link = href

            results.append((title, clean_link))
        return results
    except Exception as e:
        return [("Error occurred while fetching results", str(e))]
