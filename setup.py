from setuptools import setup, find_packages

setup(
    name="pyside6-vulnerability-tool",
    version="1.0.0",
    description="Ferramenta de Teste de Vulnerabilidades com PySide6",
    author="Desenvolvedor",
    author_email="dev@example.com",
    packages=find_packages(),
    install_requires=[
        "PySide6==6.9.2",
    ],
    python_requires=">=3.11",
    entry_points={
        "console_scripts": [
            "vulnerability-tool=src.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)

