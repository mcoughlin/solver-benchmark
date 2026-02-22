#!/usr/bin/env python
"""Benchmark a maximum weighted coverage problem with various solver libraries."""

import cvxpy
import docplex.mp.model
import linopy
import numpy as np
import pytest


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
    return nx, ny, k, w, edge_i, edge_j


def mwc_docplex(nx, ny, k, w, edge_i, edge_j):
    with docplex.mp.model.Model() as m:
        x = m.binary_var_list(nx)
        y = m.binary_var_list(ny)
        m.maximize(m.scal_prod_vars_all_different(y, w))
        m.add_constraint_(m.sum_vars_all_different(x) <= k)
        m.add_constraints_(
            m.sum_vars_all_different(x[i] for i in edge_i[edge_j == j]) >= y[j]
            for j in range(ny)
        )
        solution = m.solve()
        return solution.get_values(x)


def mwc_cvxpy(nx, ny, k, w, edge_i, edge_j):
    x = cvxpy.Variable(nx, boolean=True)
    y = cvxpy.Variable(ny, boolean=True)
    problem = cvxpy.Problem(
        cvxpy.Maximize(y @ w),
        [
            x.sum() <= k,
            *[cvxpy.sum(x[i] for i in edge_i[edge_j == j]) >= y[j] for j in range(ny)],
        ],
    )
    problem.solve(solver="cplex")
    return x.value


def mwc_linopy(nx, ny, k, w, edge_i, edge_j):
    m = linopy.Model()
    x = m.add_variables(coords=[np.arange(nx)], binary=True)
    y = m.add_variables(coords=[np.arange(ny)], binary=True)
    m.add_constraints(x.sum() <= k)
    for j in range(ny):
        m.add_constraints(x.loc[edge_i[edge_j == j]].sum() >= y[j])
    m.add_objective(y @ w, sense="max")
    m.solve(solver_name="cplex")
    return x.solution


@pytest.mark.parametrize("solver", [mwc_docplex, mwc_cvxpy, mwc_linopy])
def test_docplex(example_problem, solver, benchmark):
    benchmark(solver, *example_problem)


if __name__ == "__main__":
    pytest.main([__file__, "--benchmark-sort=fullname", "-xvv"])
