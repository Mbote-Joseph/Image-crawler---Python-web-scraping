import urllib.request
from bs4 import BeautifulSoup as bs


def extract_dp():
    url = f'https://www.instagram.com/{user_name}/'
    print(f'Connecting to profile {url}')
    try:
        response = urllib.request.urlopen(url).read()
        soup = bs(response, 'html.parser')
        meta = soup.find_all('meta', {'property': 'og:image'})  # extracts meta tag for property og:image (profile pic)
        img_src = meta[0]['content']
        name = url.split('/')[-2]
        img_name = f'{name}.jpg'
        urllib.request.urlretrieve(img_src, img_name)
        print(f'Downloaded image has been saved as {img_name}')
    except:
        print(f"Unable to connect to '{user_name}'. Make sure the username is correct.")


if __name__ == '__main__':
    user_name = input('Enter the username:\n')
    extract_dp()