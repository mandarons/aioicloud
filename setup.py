from codecs import open

from setuptools import find_packages, setup

REPO_URL = "https://github.com/mandarons/aioicloud"
VERSION = "0.0.0"

with open("README.md") as fh:
    long_description = fh.read()
with open("requirements.txt") as fh:
    required = fh.read().splitlines()

setup(
    name="aioicloud",
    version=VERSION,
    author="Mandar Patil",
    author_email="mandarons@pm.me",
    # TODO: update description
    description="Python library to ...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_URL,
    package_dir={".": ""},
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=required,
    # TODO remove if there is no entry point
    entry_points="""
    [console_scripts]
    icloud=aioicloud.cmdline:main
    """,
)
