from setuptools import setup, find_packages


def read_requirements(file_name):
    with open(file_name) as _file:
        requirements = _file.readlines()

    requirements = [requirement.strip()
                    for requirement in
                    requirements]

    return requirements


setup(
    name="feature_scaling",
    python_requires=">3.6",
    version="1.0.0",
    description="feature scaling and unscaling component",
    url="https://github.com/Raiz-Environmental-Technology/feature_scaling.git",
    author="Raiz Environmental Technology",
    author_email="contato@raiz.site",
    license="BSD2",
    include_package_data=True,
    packages=find_packages(exclude=[".venv", "tests"]),
    install_requires=read_requirements("requirements/prod.txt"),
    extras_require={
        "dev": read_requirements("requirements/dev.txt")
    }
)
