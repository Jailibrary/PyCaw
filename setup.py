import setuptools

with open("docs/index.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycaw",
    version="0.0.1",
    author="Jailibrary",
    author_email="admin@jailibrary.com",
    description="A Cydia/Sileo package and repository Python wrapper.",
    long_description=long_description,
    long_description_content_type="text/reStructuredText",
    url="https://github.com/Jailibrary/PyCaw",
    install_requires=[
        'requests'
    ],
    packages=setuptools.find_packages()
)
