from setuptools import setup, find_packages

with open("../README-20251225175800.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("../requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="cv-face-detection",
    version="1.0.0",
    author="Stetson Perceptron",
    author_email="stetson@example.com",
    description="Face detection using Haar cascades in OpenCV",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KSP-Hub/My-CV-Engineering-Projects/CV-010_face_detection",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    package_data={
        "": ["configs/*.xml"]
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "face-detection=face_detection:main",
            "cv-face-app=CV-010-app:main",
        ],
    },
)