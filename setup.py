import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata2-drewrust", # Replace with your own username
    version="0.1.3",
    author="drewrust",
    author_email="drewrust1@gmail.com",
    description="A collection of beginner utilites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrewRust/lambdata2-drewrust",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)