import setuptools

with open("Readme.md","r",encoding="utf-8") as f :
    long_description = f.read()


__version__="0.0.1"

REPO_NAME= "wine_quality_prediction"
USER_NAME= "Soura10"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "souradeeproy.10@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    Long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)