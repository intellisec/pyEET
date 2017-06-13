import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "eet",
    version = "0.3.0",
    author = "Zdenek Travnicek",
    author_email = "v154c1@gmail.com",
    description = ("A simple implementation of EET (Electronic records of sales) for Czech Financial Administration"),
    license = "BSD",
    keywords = "EET",
    url = "https://github.com/v154c1/pyEET",
    packages=['eet'],
    install_requires=[
          'lxml<3.9.0',
          'pyopenssl<17.1.0',
          'pytz<2018',
          'requests<2.18.0',
      ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)