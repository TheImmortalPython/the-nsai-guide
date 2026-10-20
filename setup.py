from setuptools import setup, find_packages

setup(
    name="the-nsai-guide",
    version="0.1.0",
    author="Joshua St. Germain",
    author_email="theimmortalpythonlabs@proton.me",
    description="Educational guide and architecture for Non-Stochastic AI (NSAI).",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "torch>=2.0.0",
        "transformers>=4.30.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
