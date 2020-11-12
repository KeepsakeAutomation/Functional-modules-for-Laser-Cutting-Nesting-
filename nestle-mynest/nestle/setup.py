import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nestle-mynest",
    version="2.8.1",
    description="Trial library for nesting and laser cutting",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/Harsheel15/modules-for-laser-cutting/tree/master/Nestlibtrial",
    Maintainer="Tirth, Harshil, Shailee",
    author="HaShTi",
    author_email="hashtishah@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    packages=["mynest"],
    include_package_data=True,
    install_requires=["matplotlib", "svglib", "reportlab",  "pathlib", "setuptools"],
)
