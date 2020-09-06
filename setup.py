from setuptools import setup, find_packages


def read_requirements(file_name):
    with open(file_name) as _file:
        requirements = _file.readlines()

    requirements = [requirement.strip()
                    for requirement in
                    requirements]

    return requirements

# feature_scaling


setup(
    name="feature_scaling",
    version="1.0.0",
    description="",
    packages=find_packages(exclude=[".venv", "Tests"]),
    include_package_data=True,
    install_requires=read_requirements("requirements/prod.txt"),
    extras_require={
        "dev": read_requirements("requirements/dev.txt")
    }
)
