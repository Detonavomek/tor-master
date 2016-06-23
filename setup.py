import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "tor_pool",
    version = "1.0",
    author = "detonavomek",
    author_email = "detonavomek@gmail.com",
    description = ("Pool Tors controller"),
    license = "BSD",
    keywords = "tor controller",
    url = "http://github.com/Detonavomek/tor-pool",
    packages=['tor-pool'],
    long_description=read('README.md'),
    install_requires=[
        "Jinja2==2.8",
        "stem==1.4.0"
    ],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
