from setuptools import setup

setup_kwargs = dict(
    name="netsuite",
    version="0.5.4",
    description="Wrapper around Netsuite SuiteTalk SOAP/REST Web Services and Restlets",
    packages=["netsuite"],
    include_package_data=True,
    author="Jacob Magnusson",
    author_email="m@jacobian.se",
    url="https://github.com/cart-com/netsuite",
    license="MIT",
    platforms="any",
    install_requires=["requests-oauthlib", "zeep", "orjson", "httpx==0.12.0", "authlib"],
    extras_require=extras_require,
    entry_points={"console_scripts": ["netsuite = netsuite.__main__:main",],},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)

if __name__ == "__main__":
    setup(**setup_kwargs)
