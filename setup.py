from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="onion_network",
    version="1.0",
    description="A module for generating and visualizing onion-structured networks!",
    long_description=long_description,
    author="Simon Popelier",
    author_email="simon.popelier@gmail.com",
    packages=["onion_network"],
    install_requires=["wheel", "bar", "greek"],
)
