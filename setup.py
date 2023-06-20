import setuptools


#Read the content of the readme.md file and assign it to the description variable
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# Define variables to store the version, the repo name, user name, source project and email address.
__version__ = "0.0.0"

REPO_NAME = "chicken_classification"
AUTHOR_USER_NAME = "amira123bd"
SRC_REPO = "myproject"
AUTHOR_EMAIL = "bedouiamira123@gmail.com"


# using setuptools.setup to configure and define the details of the package
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for a classification task ",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    ## this help to find packages in src directories
    packages=setuptools.find_packages(where="src")
)