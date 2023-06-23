from setuptools import find_packages, setup
import io
import os

with open("README.md", "r") as f:
    long_description = f.read()


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="onion_network",
    version="1.0",
    description="A module for generating and visualizing onion-structured networks!",
    long_description=long_description,
    author="Simon Popelier",
    author_email="simon.popelier@gmail.com",
    packages=["onion_network"],
    install_requires=read_requirements("requirements.txt"),
)
