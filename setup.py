import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="orka-sdk",
    version="1.0.2",
    description="Control Orka clusters and the macOS VMs they run.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jeff-vincent/orka-python-sdk",
    author="Jeff Vincent",
    author_email="jeff.d.vincent@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=["orka_sdk"],
    include_package_data=True,
    install_requires=[
        "attrs==21.4.0",
        "bcrypt==3.2.0",
        "cachetools==4.2.4",
        "certifi==2021.10.8",
        "cffi==1.15.0",
        "charset-normalizer==2.0.9",
        "cryptography==36.0.0",
        "google-auth==2.3.3",
        "idna==3.3",
        "importlib-metadata==4.10.1",
        "iniconfig==1.1.1",
        "Jinja2==3.0.3",
        "kubernetes==21.7.0",
        "MarkupSafe==2.0.1",
        "mock==4.0.3",
        "oauthlib==3.1.1",
        "packaging==21.3",
        "paramiko==2.8.1",
        "pluggy==1.0.0",
        "py==1.11.0",
        "pyasn1==0.4.8",
        "pyasn1-modules==0.2.8",
        "pycparser==2.21",
        "PyNaCl==1.4.0",
        "pyparsing==3.0.7",
        "pytest==6.2.5",
        "python-dateutil==2.8.2",
        "PyYAML==6.0",
        "requests==2.26.0",
        "requests-oauthlib==1.3.0",
        "rsa==4.8",
        "six==1.16.0",
        "toml==0.10.2",
        "typing_extensions==4.0.1",
        "urllib3==1.26.7",
        "websocket-client==1.2.3",
        "zipp==3.7.0"
        ]
)