# setup.py file


from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="lambdata_TerrenceMaloneII",
    version="2.5",
    author="Terrence Malone",
    author_email="tamalone87@gmail.com",
    description="Assignment 1",
    long_description=long_description,
    long_description_content_type="text/markdown",
    #License=""
    url="https://github.com/TerrenceAm22/DS-Unit-3-Sprint-1-Software-Engineering/tree/master/module1-python-modules-packages-and-environments/my_lambdata2",
    packages=find_packages()
)