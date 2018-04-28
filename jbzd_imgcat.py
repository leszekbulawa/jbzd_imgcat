import random
import requests
from bs4 import BeautifulSoup
from base64 import b64encode
from sys import stdout


def get_jbzd_random_url():
    r = requests.get('https://jbzd.pl')
    soup = BeautifulSoup(r.text, 'html.parser')
    urls = soup.findAll("img", class_="resource-image")
    draw_url = urls[random.randint(0, len(urls) - 1)].attrs['src']
    return draw_url


def get_image_content(url):
    return requests.get(url).content


def print_image(data):
    image_b64_data = b64encode(data)
    image_size = str(len(image_b64_data))
    header = bytes('\033]1337;File=;size={};inline=1:'.format(image_size).encode('utf-8'))
    stdout.buffer.write(header + image_b64_data + b'\a\n')


def main():
    print_image(get_image_content(get_jbzd_random_url()))
