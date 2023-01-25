import setuptools

with open("README.md", "r", encoding = "utf-8") as file:
    long_description = file.read()

setuptools.setup(
    name = "one-pyece",
    version = "0.0.1",
    author = "Rémi JARA",
    author_email = "remi.jara4@gmail.com",
    description = "A package to use the One-Piece API : https://api-onepiece.com/",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "package URL",
    project_urls = {
        "Bug Tracker": "package issues URL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)