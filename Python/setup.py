import setuptools

setuptools.setup(
    name="volisha"
    version ="0.0.1"
    author="Shefali Lachhar"
    author_email="isha15lachhar@gmail.com"
    description="expenditure calculator"
    url=""
    project_urls={"Bug Tracker":""
    },
classifiers=[
    "Programming Language::Python::3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"

],
package_dir ={"","src"},
packages=setuptools.find_packages(where="src"),
python_requires =">=3.6",
)