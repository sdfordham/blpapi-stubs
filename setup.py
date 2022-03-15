from setuptools import setup


setup(
    name="blpapi-stubs",
    version="1.0",
    description="Mypy stubs for blpapi-python",
    author="Stiofán Fordham",
    author_email="stiofan.fordham@gmail.com",
    install_requires=["mypy>=0.790", "typing-extensions>=3.7.4"],
    packages=["blpapi"],
    package_data={"": ["*.pyi", "py.typed"]},
)
