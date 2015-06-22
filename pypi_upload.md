# Notes on publishing to pypi

Make sure you have a ~/.pypirc configuration file.

```
[distutils]
index-servers =
    pypi
    pypitest

[pypi]
repository: https://pypi.python.org/pypi
username: natm
password:

[pypitest]
repository: https://testpypi.python.org/pypi
username: natm
password:
```

## Test

```
$ python setup.py register -r pypitest
$ python setup.py sdist upload -r pypitest
```

## Production

```
$ python setup.py register -r pypi
$ python setup.py sdist upload -r pypi
```
