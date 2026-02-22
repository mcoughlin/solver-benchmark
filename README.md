# Solver Benchmarks

Benchmarks for various high-level MILP solver libraries.

```
$ python test_benchmark.py
================================================================= test session starts =================================================================
platform darwin -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0 -- /Users/lpsinger/src/solver-benchmark/.venv/bin/python
cachedir: .pytest_cache
benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /Users/lpsinger/src/solver-benchmark
configfile: pyproject.toml
plugins: benchmark-5.2.3
collected 9 items

test_benchmark.py::test_docplex[0-mwc_docplex] PASSED                                                                                                                                      [ 11%]
test_benchmark.py::test_docplex[0-mwc_cvxpy] PASSED                                                                                                                                        [ 22%]
test_benchmark.py::test_docplex[0-mwc_linopy] PASSED                                                                                                                                       [ 33%]
test_benchmark.py::test_docplex[1-mwc_docplex] PASSED                                                                                                                                      [ 44%]
test_benchmark.py::test_docplex[1-mwc_cvxpy] PASSED                                                                                                                                        [ 55%]
test_benchmark.py::test_docplex[1-mwc_linopy] PASSED                                                                                                                                       [ 66%]
test_benchmark.py::test_docplex[2-mwc_docplex] PASSED                                                                                                                                      [ 77%]
test_benchmark.py::test_docplex[2-mwc_cvxpy] PASSED                                                                                                                                        [ 88%]
test_benchmark.py::test_docplex[2-mwc_linopy] PASSED                                                                                                                                       [100%]


---------------------------------------------------------------------------------------------- benchmark: 9 tests ----------------------------------------------------------------------------------------------
Name (time in ms)                      Min                   Max                  Mean              StdDev                Median                 IQR            Outliers       OPS            Rounds  Iterations
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_docplex[0-mwc_cvxpy]           5.2803 (1.0)         31.3112 (4.42)         5.8851 (1.0)        2.4244 (6.32)         5.5998 (1.0)        0.2087 (1.0)           2;7  169.9206 (1.0)         115           1
test_docplex[0-mwc_docplex]         5.3442 (1.01)         7.0898 (1.0)          5.9118 (1.00)       0.3834 (1.0)          5.7835 (1.03)       0.5041 (2.42)         18;1  169.1542 (1.00)         67           1
test_docplex[0-mwc_linopy]         94.3715 (17.87)      119.8443 (16.90)       98.6208 (16.76)      8.6690 (22.61)       95.0982 (16.98)      2.8297 (13.56)         1;1   10.1398 (0.06)          8           1
test_docplex[1-mwc_cvxpy]         229.9482 (43.55)      268.6119 (37.89)      244.0977 (41.48)     17.4128 (45.41)      233.9085 (41.77)     28.2754 (135.46)        1;0    4.0967 (0.02)          5           1
test_docplex[1-mwc_docplex]        11.3469 (2.15)        16.6823 (2.35)        12.7187 (2.16)       1.0717 (2.80)        12.4510 (2.22)       0.9343 (4.48)         14;6   78.6244 (0.46)         59           1
test_docplex[1-mwc_linopy]        802.9581 (152.07)     816.4862 (115.16)     809.6799 (137.58)     6.0510 (15.78)      806.9851 (144.11)    10.4400 (50.02)         2;0    1.2351 (0.01)          5           1
test_docplex[2-mwc_cvxpy]       4,914.0526 (930.64)   5,186.7748 (731.58)   5,049.3532 (857.99)   118.5766 (309.26)   5,016.6865 (895.88)   208.5613 (999.19)        2;0    0.1980 (0.00)          5           1
test_docplex[2-mwc_docplex]       126.6008 (23.98)      135.4649 (19.11)      128.9475 (21.91)      3.3525 (8.74)       127.4693 (22.76)      2.4399 (11.69)         1;1    7.7551 (0.05)          6           1
test_docplex[2-mwc_linopy]      7,996.3758 (>1000.0)  8,094.5902 (>1000.0)  8,044.9115 (>1000.0)   43.1270 (112.48)   8,027.8987 (>1000.0)   74.3107 (356.01)        2;0    0.1243 (0.00)          5           1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================= 9 passed in 104.58s (0:01:44) ==================================================================================
```
