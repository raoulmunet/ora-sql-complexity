# ora-sql-complexity

[![tests](https://github.com/raoulmunet/ora-sql-complexity/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-sql-complexity/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Measure structural features of Oracle SQL and produce a transparent heuristic complexity summary.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Common SQL structures |
> | Oracle Database 23ai | ✅ Common SQL structures |
> | Oracle AI Database 26ai | ✅ Common SQL structures |
>
> Version-specific syntax not recognized by the lightweight scanner may be under-counted. The raw metrics remain more important than the summary label.

## Metrics

- referenced tables;
- JOIN count;
- subquery count;
- CTE count;
- CASE expressions;
- aggregate functions;
- analytic/window functions;
- UNION / INTERSECT / MINUS operations;
- GROUP BY / ORDER BY;
- approximate nesting depth.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-sql-complexity.git"

ora-sql-complexity examples/report.sql
ora-sql-complexity examples/report.sql --format json
```

Example:

```text
Tables: 4
Joins: 3
Subqueries: 1
CTEs: 2
CASE: 3
Window functions: 2
Structural score: 21
Band: high
```

## About the score

The score is **not a scientific measure of query quality or performance**. It is a documented weighted summary intended for code-review triage. A high score can describe perfectly good SQL; a short query can still perform badly.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
