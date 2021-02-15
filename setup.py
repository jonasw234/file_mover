import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="file_mover",
    version="0.1.0",
    author="Jonas A. Wendorf",
    description="Moves/copies a number of random files from one directory to another.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jonasw234/file_mover",
    packages=setuptools.find_packages(),
    install_requires=["docopt", "schema"],
    include_package_data=True,
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3)",
        "Operating System :: Linux",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.6.9",
    entry_points={
        "console_scripts": ["file_mover=file_mover.file_mover:main"],
    },
)
