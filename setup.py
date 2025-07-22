#!/usr/bin/env python
# to build:
# ON WINDOWS:
# package testing deps: pip install -r requirements.txt
# testing: cd ./python_src >>> pip install -e .
# building: python setup.py sdist bdist_wheel
# publishing: twine upload dist/*
# verify install: pip list | findstr icmobi_model
# NOTE: make sure venv is activated in VSCode (ctrl+shift+P)

# ON UBUNTU:
# pip install -e .

import os
from setuptools import setup, Command, find_packages

class CleanCommand(Command):
    """Custom clean command to tidy up the project root."""
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        # os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')
        os.system('rmdir /S /Q .\\build .\\dist')
        os.system('del /S  **.pyc')
        os.system('del /S  **.tgz')
        os.system('del /S  **.egg-info')
        
setup(
    name="runescape_bot",
    version="0.1.0",
    description="A brief description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Jacob Salminen",
    author_email="jsalminen14@gmail.com",
    url="https://github.com/JacobSal/Runescape_Bot.git",
    packages=find_packages("","icmobi_ext"),
    include_package_data=True,
    install_requires=["pyautogui",
                      "numpy",
                      "pillow",
                      "opencv-python",
                      "scipy",
                      "matplotlib"
        # Add your dependencies here
        # e.g., "numpy>=1.18.0", "scipy>=1.5.0"
    ],
    cmdclass={
        'clean': CleanCommand,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
