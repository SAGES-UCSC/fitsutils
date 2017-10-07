from setuptools import setup

setup(
    name="fitsutils",
    version="0.0.1",
    description="Assorted fits file utilities",
    url="https://github.com/adwasser/fitsutils",
    author="Asher Wasserman",
    author_email="adwasser@ucsc.edu",
    license="MIT",
    install_requires=['astropy'],
    scripts=["fitscrop", "fitscphdr"])

