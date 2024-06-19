# setup.py

from setuptools import setup, find_packages

setup(
    name="rut_validator",
    version="0.1",
    packages=find_packages(),
    description="A simple library to validate Chilean RUTs",
    author="Tu Nombre",
    author_email="tu.email@example.com",
    url="https://github.com/tuusuario/rut_validator",  # URL de tu repositorio
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[],
    test_suite='tests',
)
