#!/usr/bin/env python
"""Benchmark a maximum weighted coverage problem with various solver libraries."""

import cvxpy
import docplex.mp.model
import linopy
import numpy as np
import pandas as pd
import pytest
import xarray as xr
from scipy.sparse import csc_matrix


@pytest.fixture(scope="module", params=range(3))
def example_problem(request):
    order = request.param
    mult = 10**order
    nx = 10 * mult
    ny = 10 * mult
    ncons = 1000 * mult
    k = mult

    rng = np.random.default_rng(42)
    w = rng.uniform(0, 1, size=ny)
    edge_i, edge_j = np.unique(
        np.vstack((rng.choice(nx, ncons), rng.choice(ny, ncons))), axis=1
    )
    assign = [edge_i[edge_j == j] for j in range(ny)]
    A = csc_matrix((np.ones(len(edge_i)), (edge_j, edge_i)), shape=(ny, nx))

    return nx, ny, k, w, assign, A


def mwc0_docplex(nx, ny, k, w, assign, A):
    with docplex.mp.model.Model() as m:
        x = np.asarray(m.binary_var_list(nx))
        y = np.asarray(m.binary_var_list(ny))
        m.maximize(m.scal_prod_vars_all_different(y, w))
        m.add_constraint_(m.sum_vars_all_different(x) <= k)
        m.add_constraints_(
            m.sum_vars_all_different(x[i]) >= y[j] for j, i in enumerate(assign)
        )
        solution = m.solve()
        return solution.get_values(x)


def mwc1_cvxpy(nx, ny, k, w, assign, A):
    x = cvxpy.Variable(nx, boolean=True)
    y = cvxpy.Variable(ny, boolean=True)
    problem = cvxpy.Problem(
        cvxpy.Maximize(y @ w),
        [x.sum() <= k, A @ x >= y],
    )
    problem.solve(solver="cplex")
    return x.value


def mwc2_linopy(nx, ny, k, w, assign, A):
    m = linopy.Model()
    x = m.add_variables(coords=[pd.RangeIndex(nx, name="i")], binary=True, name="x")
    y = m.add_variables(coords=[pd.RangeIndex(ny, name="j")], binary=True, name="y")
    m.add_constraints(x.sum() <= k)
    A_xr = xr.DataArray(A.toarray(), dims=["j", "i"])
    m.add_constraints(((A_xr * x).sum("i") >= y))
    m.add_objective(y @ w, sense="max")
    m.solve(solver_name="cplex")
    return x.solution


@pytest.mark.parametrize("solver", [mwc0_docplex, mwc1_cvxpy, mwc2_linopy])
def test_docplex(example_problem, solver, benchmark):
    benchmark(solver, *example_problem)


if __name__ == "__main__":
    pytest.main([__file__, "--benchmark-sort=fullname", "-xvv"])
