import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = '0.0.0'

REPO_NAME = 'CNN_classifier'
AUTHOR_USER_NAME = 'Rahul'
AUTHOR_EMAIL = 'rahultawar2004@gmail.com'
SRC_REPO = 'CNN_classifier'

setuptools.setup(
    name=SRC_REPO,
    version=version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)