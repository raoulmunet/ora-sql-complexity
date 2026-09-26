# ora-sql-complexity

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

## License

MIT.
