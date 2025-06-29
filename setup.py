from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="flashcard-creator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A time-efficient desktop application for creating Anki-style flashcards compatible with Obsidian's Space Repetition plugin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/flashcard-creator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Education",
        "Topic :: Software Development :: User Interfaces",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "flashcard-creator=templater:main",
        ],
    },
    include_package_data=True,
    keywords="flashcards, obsidian, spaced-repetition, anki, education, study-tools",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/flashcard-creator/issues",
        "Source": "https://github.com/yourusername/flashcard-creator",
        "Documentation": "https://github.com/yourusername/flashcard-creator#readme",
    },
) 