import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jekbook",
    version="0.0.1",
    author="idrisr",
    author_email="id@hippoplant.com",
    description="It's an exporter for jupyter with jekyll"
    long_description=long_description,
    url="https://github.com/idrisr/jekbook",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
