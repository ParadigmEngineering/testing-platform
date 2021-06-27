# testing-platform
This tool will be used to create digital twins of all the devices in the boring system.

## Python Development 
Although not absolutely necessary, it is highly recommended you work out of a python virtual environment. It doesnt matter what tool you use for this, one example uses
the standard python venv module. 

**Note**: Python 3.8+ is required.
```
cd {REPO_LOCATION}/testing-platform
python3 -m venv .venv

Windows |  \.venv\Scripts\activate 
Unix    |  .venv/bin/activate
```

Install third-party python dependencies
```
cd {REPO_LOCATION}/testing-platform
pip install -r requirements.txt
```

Install the project python package (in development mode)
```
cd {REPO_LOCATION}
pip install -e testing-platform 
```

To uninstall the package
```
pip uninstall testing-platform
```

To ensure all packages were correctly installed
```
pip freeze
```

To ensure custom packages are correctly installed, attempt to import the example package. The output should be as seen below
```
python3
>> import pkgexample
>> EXAMPLE PACKAGE IMPORTED - INSTALLATION VALID
```