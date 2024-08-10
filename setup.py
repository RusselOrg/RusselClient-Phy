from setuptools import setup, find_packages

setup(
    name="russelCache-client",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests","aiohttp"
    ],
    description="A Python client for interacting with a russelCache cache server",
    author="Saeed Safi",
    author_email="safi.saeed1999@gmail.com",
)
