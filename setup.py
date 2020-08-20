import setuptools


with open("README.md", "r") as file:
    long_description = file.read()


setuptools.setup(
    name="mkignore",
    version="0.1.3",
    author="Emanuel Claesson",
    author_email="emanuel.claesson@gmail.com",
    description="Generate .gitignore files from templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EClaesson/mkignore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    install_requires=[
        'dload>=0.6',
    ],
    entry_points={
        'console_scripts': ['mkignore=mkignore:main'],
    },
)
