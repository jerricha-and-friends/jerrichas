from setuptools import setup
improt os, shutil

VERSION = "0.2.0"

setup(version = VERSION,
    description = "Jerrichas, the ParagonChat DB tool and API",
    packages = [
        "jerrichas",
    ],
    scripts = [
        "jerrichas.py",
    ],
    author="Jerricha",
    install_requires = [],
    license = "GPLv3",
)
