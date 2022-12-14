from setuptools import find_packages, setup

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Preet Garach",
    author_email = "preetgarach@gmail.com",
    packages = find_packages(),
    install_requires = [],
)
setup(
    name="sensor",
    version="0.0.1",
    author="ineuron",
    author_email="avnish@ineuron.ai",
    packages = find_packages(),
    install_requires = ["pymongo==4.2.0"],
)