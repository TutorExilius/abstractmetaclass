import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="abstractmetaclass",
    version="0.0.1",
    author="Tutor Exilius",
    author_email="tutorexilius@gmail.com",
    description="A small metaclass, which enforce subclasses to implement methods with same signature from derived abstract class(es).",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tutorexilius/abstractmetaclass",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
