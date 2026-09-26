from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import measure

def main(argv=None):
    p=argparse.ArgumentParser(description="Measure Oracle SQL structural complexity.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json"),default="text")
    a=p.parse_args(argv)
    m=measure(Path(a.source).read_text(encoding="utf-8"))
    if a.format=="json":
        print(json.dumps(m.to_dict(),indent=2))
    else:
        labels=[
            ("Tables",m.tables),("Joins",m.joins),("Subqueries",m.subqueries),("CTEs",m.ctes),
            ("CASE",m.cases),("Aggregates",m.aggregates),("Window functions",m.windows),
            ("Set operations",m.set_operations),("Max parenthesis depth",m.max_parenthesis_depth),
            ("Structural score",m.score),("Band",m.band)
        ]
        for k,v in labels: print(f"{k}: {v}")
    return 0
if __name__=="__main__": raise SystemExit(main())
