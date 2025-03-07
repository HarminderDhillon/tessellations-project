from setuptools import setup, find_packages

setup(
    name="tessellations",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pillow>=10.2.0",
        "numpy>=1.26.3",
        "matplotlib>=3.8.2",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "black>=23.12.1",
            "isort>=5.13.2",
            "flake8>=6.1.0",
        ],
    },
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "tessellate=tessellations.cli.main:main",
        ],
    },
)