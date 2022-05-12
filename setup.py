import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="wake-me",
    version="1.0.0",
    description="A simple command line alarm clock to remind you everything!",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tubbadu/wake-me",
    author="Tubbadu",
    author_email="tubbadu@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["scripts"],
    include_package_data=True,
    install_requires=[],
    entry_points={
        "console_scripts": [
            "wake-me=scripts.__main__:main",
        ]
    },
)
 
