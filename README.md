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


#### Example

```python
from nonogram_solver import solve_nonogram

result = solve_nonogram(
    [[1, 1, 2], [1, 2], [6], [1]],
    [[3], [2], [1, 1], [2], [3], [1, 1]],
)
for row in result:
    print(' '.join(str(i) for i in row))
```