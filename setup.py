import setuptools


with open("README.md", "r") as setup:
    long_description = setup.read()

setuptools.setup(
    name="shadowrun",
    version="1.982.2",
    author="Dhruv Maaniya (@midnightmadwalk)",
    author_email="midnightmadwalk@gmail.com",
    description="pyhton interaction with heroku website.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shadowrun/shadowrun",
    license="MIT",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['aiohttp', 'apscheduler'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
