import pathlib
from setuptools import find_packages, setup

BASE_DIR = pathlib.Path(__file__).parent

README = (BASE_DIR / "README.md").read_text()

setup(
   name='sajilo-orm',
   version='0.0.6',
   description='Sarai Sajilo lightweight ORM inspired by Django ORM with nepali twist',
   long_description=README,
   long_description_content_type="text/markdown",
   url='https://github.com/learningnoobi/sajilo-orm',
   author='learningnoobi (Bishal Rai)',
   author_email='fanime492@gmail.com',
   license='MIT',
   packages=find_packages(exclude=['tests*']),
   include_package_data=True,
   classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent"
    ],
   install_requires=[
    "colorama ~= 0.4.4",  
    "iniconfig ~= 1.1.1",
    "mypy-extensions ~= 0.4.3",
    "packaging ~= 21.3",
    "pathspec ~= 0.9.0",
    "platformdirs ~= 2.5.2",
    "pluggy ~= 1.0.0",
    "psycopg2-binary ~= 2.9.3",
    "py ~= 1.11.0",
    "pyparsing ~= 3.0.8",
    "tomli ~= 2.0.1",
   ],
   python_requires=">=3.6",
   zip_safe=False,
   extras_require = {
        "dev": [
            "coverage==6.3.2",
           "pytest==7.1.2"
        ]
    }
)



    