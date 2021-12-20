import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="upload_to_cloud",
    version="0.0.1",
    author="Delvin",
    author_email="delvinpkty@gmail.com",
    description="Package to upload directory to cloud storages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/delvinp/upload_to_cloud",
    project_urls={
        "Bug Tracker": "",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["google-cloud-storage", "boto3"],
)
