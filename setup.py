from setuptools import setup, find_packages

setup(
    name="python_programing_demo_app",
    version="0.0.1",
    packages=find_packages(),
    package_data={"roboter": ["templates/*.txt"]},
    license="MIT",
    author="liber",
    author_email="example@example.com",
    install_requires={"termcolor"},
    description="roboter description"
)