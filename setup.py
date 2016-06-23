import os
from setuptools import setup


setup(
    name = "tor_pool",
    version = "1.0.1",
    author = "detonavomek",
    author_email = "detonavomek@gmail.com",
    description = ("Pool Tors controller"),
    license = "BSD",
    keywords = "tor controller",
    url = "http://github.com/Detonavomek/tor-pool",
    packages=['tor_pool'],
    long_description="Pool Tors controller",
    install_requires=[
        "Jinja2==2.8",
        "stem==1.4.0"
    ],
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
