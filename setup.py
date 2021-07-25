import setuptools

setuptools.setup(
    name="x735-v2.5",
    version="0.0.1",
    description="Library for board x735",
    author="sh.kiruh@gmail.com",
    install_requires=[
        "pigpio",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
    ],
    entry_points={
        "console_scripts": ["pwm_fan_control=pwm_fan_control"],
    },
)
