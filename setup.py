import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="project_python",
    version="0.0.1",
    author="Geraud AZANGUE",
    author_email="geraudnguetsebaudouin@gmail.com",
    description="A small test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geraudazangue/Python_Projects.git",
    packages=setuptools.find_packages("put_allpacakge_here),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
