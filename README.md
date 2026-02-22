# Solver Benchmarks

Benchmarks for various high-level MILP solver libraries.

```
$ ./test_benchmark.py
====================================================================================== test session starts =======================================================================================
platform darwin -- Python 3.11.14, pytest-9.0.2, pluggy-1.6.0 -- /Users/lpsinger/src/solver-benchmark/.venv/bin/python
cachedir: .pytest_cache
benchmark: 5.2.3 (defaults: timer=time.perf_counter disable_gc=False min_rounds=5 min_time=0.000005 max_time=1.0 calibration_precision=10 warmup=False warmup_iterations=100000)
rootdir: /Users/lpsinger/src/solver-benchmark
configfile: pyproject.toml
plugins: benchmark-5.2.3
collected 9 items

test_benchmark.py::test_docplex[0-mwc0_docplex] PASSED                                                                                                                                     [ 11%]
test_benchmark.py::test_docplex[0-mwc1_cvxpy] PASSED                                                                                                                                       [ 22%]
test_benchmark.py::test_docplex[0-mwc2_linopy] PASSED                                                                                                                                      [ 33%]
test_benchmark.py::test_docplex[1-mwc0_docplex] PASSED                                                                                                                                     [ 44%]
test_benchmark.py::test_docplex[1-mwc1_cvxpy] PASSED                                                                                                                                       [ 55%]
test_benchmark.py::test_docplex[1-mwc2_linopy] PASSED                                                                                                                                      [ 66%]
test_benchmark.py::test_docplex[2-mwc0_docplex] PASSED                                                                                                                                     [ 77%]
test_benchmark.py::test_docplex[2-mwc1_cvxpy] PASSED                                                                                                                                       [ 88%]
test_benchmark.py::test_docplex[2-mwc2_linopy] PASSED                                                                                                                                      [100%]


----------------------------------------------------------------------------------------------- benchmark: 9 tests ----------------------------------------------------------------------------------------------
Name (time in ms)                       Min                   Max                  Mean              StdDev                Median                 IQR            Outliers       OPS            Rounds  Iterations
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_docplex[0-mwc0_docplex]         5.2334 (1.31)         7.1168 (1.42)         5.7686 (1.32)       0.3355 (1.65)         5.7275 (1.32)       0.4450 (1.77)         13;2  173.3538 (0.76)         62           1
test_docplex[0-mwc1_cvxpy]           3.9805 (1.0)          5.0292 (1.0)          4.3634 (1.0)        0.2029 (1.0)          4.3422 (1.0)        0.2507 (1.0)          34;3  229.1798 (1.0)         121           1
test_docplex[0-mwc2_linopy]         94.6680 (23.78)       98.7002 (19.63)       95.7816 (21.95)      1.6743 (8.25)        95.3394 (21.96)      1.6184 (6.45)          1;0   10.4404 (0.05)          5           1
test_docplex[1-mwc0_docplex]        10.6900 (2.69)        47.9832 (9.54)        12.7266 (2.92)       4.6588 (22.96)       12.1029 (2.79)       0.9868 (3.94)          1;2   78.5757 (0.34)         61           1
test_docplex[1-mwc1_cvxpy]          30.5559 (7.68)        63.0946 (12.55)       35.7567 (8.19)       9.9398 (48.99)       31.0587 (7.15)       1.7083 (6.81)          5;6   27.9668 (0.12)         29           1
test_docplex[1-mwc2_linopy]        804.2107 (202.04)     815.3287 (162.12)     809.9377 (185.62)     3.9554 (19.49)      810.2105 (186.59)     3.6306 (14.48)         2;0    1.2347 (0.01)          5           1
test_docplex[2-mwc0_docplex]        77.7952 (19.54)      121.0663 (24.07)       85.3893 (19.57)     14.3321 (70.64)       79.9550 (18.41)      2.3472 (9.36)          2;2   11.7111 (0.05)         13           1
test_docplex[2-mwc1_cvxpy]         486.8883 (122.32)     515.0400 (102.41)     503.0700 (115.29)    14.3545 (70.75)      511.8029 (117.87)    26.3812 (105.22)        2;0    1.9878 (0.01)          5           1
test_docplex[2-mwc2_linopy]      8,034.9900 (>1000.0)  8,533.4136 (>1000.0)  8,218.3794 (>1000.0)  200.7776 (989.52)   8,117.6698 (>1000.0)  265.9063 (>1000.0)       1;0    0.1217 (0.00)          5           1
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
================================================================================== 9 passed in 72.54s (0:01:12) ==================================================================================
```
