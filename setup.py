from setuptools import setup
import os, shutil

VERSION = "0.3.1"

setup(version = VERSION,
    description = "Jerrichas, the ParagonChat DB tool and API",
    packages = [
        "jerrichas",
    ],
    scripts = [
        "Jerrichas.py",
    ],
    author="Jerricha",
    install_requires = [],
    license = "GPLv3",
)
