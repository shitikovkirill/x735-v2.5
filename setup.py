import setuptools

setuptools.setup(
    name="x735-v2.5",
    version="0.0.1",
    description="Library for board x735",
    author="sh.kiruh@gmail.com",
    install_requires=[
        "pigpio==1.78",
        "click==8.0.1",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
    ],
    entry_points={
        "console_scripts": ["x735fan=main:fan"],
    },
)
