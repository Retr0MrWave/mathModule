import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mathmodule",
    version="0.0.1",
    author="Ilia Zhuravok",
    author_email="ilia.zhuravok@gmail.com",
    description="My library with math functions and classes that might be usefull",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Retr0MrWave/mathModule",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)