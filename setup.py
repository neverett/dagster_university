from setuptools import find_packages, setup

setup(
    name="dagster_university",
    packages=find_packages(exclude=["dagster_university_tests"]),
    install_requires=[
        "dagster==1.10.2",
        "dagster-cloud",
        "dagster-duckdb",
        "matplotlib",
        "geopandas",
        "kaleido",
        "pandas",
        "plotly",
        "shapely",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
