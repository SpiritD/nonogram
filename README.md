# Nonograms

A python solver for nonogram (japan crossword puzzle).

### Install package

```shell script
python3 setup.py install
``` 

### Run tests

##### Run tests without install package

```shell script
PYTHONPATH=$PWD pytest tests
```


### Check style and typing

```shell script
flake8 nonogram_solver/
mypy nonogram_solver/
```
