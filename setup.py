import os
from setuptools import setup

setup(
    name="OnHands",
    version="0.0.1",
    author="Felipe Volpone",
    author_email="felipevolpone@gmail.com",
    description=(""),
    license = "MIT",
    keywords = "python framework onhands api rest",
    url = "http://github.com/felipevolpone/onhands",
    packages=['onhands', 'tests'],
    install_requires=['webapp2', 'webob'],
    long_description="Check on github: http://github.com/felipevolpone/onhands",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
