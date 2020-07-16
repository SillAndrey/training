import requests
import re
from bs4 import BeautifulSoup

def get_site_html(l):
    '''Function get html site and
       return it
    '''
    html = requests.get(l)
    response = html.status_code

    if response == 200:
        html = html.text
        return html
    else:
        exit(1)

def convert_html_toString(s):
    '''Conver html structure to simple string
       (str class)
    '''
    return str(s)

def match_links(s):
    '''Search links in html structure'''
    l = []
    match=re.findall(r'http(s:|:)\/\/(www.|ww2.|)([0-9a-z.A-Z-]*\.\w{2,3})',s)
    for el in match:
        l.append(el[2])
    return l

def main():
    '''main programm function'''
    link = input('Enter site link: ')
    site_html = get_site_html(link)
    site_html = convert_html_toString(site_html)
    links = match_links(site_html)
    print(links)

if __name__ == "__main__":
    main()