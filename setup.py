from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="shortterm-memory",
    version='{{VERSION_PLACEHOLDER}}',
    author="Tadiello Sébastien",
    author_email="sebastientadiello@gmail.com",
    description="Une approche pour la gestion de la mémoire à court terme dans les chatbots.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sebDtSci/ShortTerm-memory",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    #install_requires=requirements,
    install_requires=[
        "numpy>=1.21.0",
        "transformers>=4.44.0,<5.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
