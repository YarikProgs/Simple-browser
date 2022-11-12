import urllib.request
from bs4 import BeautifulSoup


def google(text):
    _ = []
    url = 'https://google.com/search?q=%s' % text.lower().replace(' ', '+')

    requests = urllib.request.Request(url)
    requests.add_header('User-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 '
                                      '(KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')
    raw_resp = urllib.request.urlopen(requests).read()

    html = raw_resp.decode("utf-8")
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.select('#search div.g')
    # print(divs)
    for div in divs:
        results = div.select('h3')

        if len(results) >= 1:
            h3 = results[0]
            _.append(h3.get_text())

    return _
