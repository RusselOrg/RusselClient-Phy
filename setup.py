from setuptools import setup, find_packages

setup(
    name="russel-client",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    description="A Python client for interacting with a russel cache server",
    author="Saeed Safi",
    author_email="safi.saeed1999@gmail.com",
)
