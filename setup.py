from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jbzd_imgcat',
    version='0.0.1rc2',
    description='jbzd.pl imgcat',
    url='https://github.com/leszekbulawa/jbzd_imgcat',
    author='Leszek Buława',
    author_email='leszekbu@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
    ],
    keywords='jbzd jbzd.pl imgcat',
    py_modules=['jbzd_imgcat'],
    install_requires=['requests', 'BeautifulSoup4'],
    entry_points={
        'console_scripts': [
            'jbzd_imgcat=jbzd_imgcat:main',
        ],
    },
)
