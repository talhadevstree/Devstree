from setuptools import setup, find_packages

setup(
    name="Devstree",  # Must be unique in TestPyPI
    version="0.1.0",
    author="Talha Shaikh",
    author_email="talhashaikh200218@gmail.com",
    description="A simple hello world package for TestPyPI",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/talhadevstree/Devstree",  # optional
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
