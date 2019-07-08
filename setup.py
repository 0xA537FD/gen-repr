# -*- coding: utf-8 -*-

import setuptools

with open(u"README.md", u"r") as f:
    long_description = f.read()

setuptools.setup(
    name=u"gen-repr",
    version=u"0.1.0",
    author=u"Peter Morawski",
    author_email=u"web@peter-morawski.de",
    keywords=u"make repr auto generate",
    description=u"Automatically generate the repr of a class with all it's fields",
    long_description=long_description,
    long_description_content_type=u"text/markdown",
    url=u"https://github.com/Peter-Morawski/gen-repr",
    test_suite=u"tests",
    py_modules=[u"genrepr"],
    license=u"MIT License",
    classifier=(
        u"Development Status :: 4 - Beta",
        u"License :: OSI Approved :: MIT License",
        u"Operating System :: OS Independent",
        u"Programming Language :: Python :: 2",
        u"Programming Language :: Python :: 2.7",
        u"Programming Language :: Python :: 3",
        u"Programming Language :: Python :: 3.0",
        u"Programming Language :: Python :: 3.1",
        u"Programming Language :: Python :: 3.2",
        u"Programming Language :: Python :: 3.3",
        u"Programming Language :: Python :: 3.4",
        u"Programming Language :: Python :: 3.5",
        u"Programming Language :: Python :: 3.6",
        u"Programming Language :: Python :: 3.7",
        u"Programming Language :: Python :: 3.8",
        u"Programming Language :: Python :: Implementation",
        u"Topic :: Software Development :: Libraries",
        u"Topic :: Software Development :: Widget Sets",
        u"Topic :: Utilities",
    ),
)
