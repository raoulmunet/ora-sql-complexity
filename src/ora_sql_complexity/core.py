from __future__ import annotations
from dataclasses import dataclass,asdict
import re
from ora_core import analyze_sql

@dataclass(frozen=True)
class Metrics:
    tables:int
    joins:int
    subqueries:int
    ctes:int
    cases:int
    aggregates:int
    windows:int
    set_operations:int
    group_by:int
    order_by:int
    max_parenthesis_depth:int
    score:int
    band:str
    def to_dict(self): return asdict(self)

def _depth(sql:str)->int:
    d=mx=0
    in_string=False
    i=0
    while i<len(sql):
        if sql[i]=="'":
            if in_string and i+1<len(sql) and sql[i+1]=="'": i+=2; continue
            in_string=not in_string
        elif not in_string and sql[i]=="(":
            d+=1; mx=max(mx,d)
        elif not in_string and sql[i]==")":
            d=max(0,d-1)
        i+=1
    return mx

def measure(sql:str)->Metrics:
    a=analyze_sql(sql)
    tables=len(a.all_objects)
    joins=len(re.findall(r"\bJOIN\b",sql,re.I))
    subqueries=max(0,len(re.findall(r"\bSELECT\b",sql,re.I))-len(a.operations))
    ctes=len(re.findall(r"(?:\bWITH\b|,)\s*[A-Za-z][\w$#]*\s+AS\s*\(",sql,re.I))
    cases=len(re.findall(r"\bCASE\b",sql,re.I))
    aggregates=len(re.findall(r"\b(?:COUNT|SUM|AVG|MIN|MAX)\s*\(",sql,re.I))
    windows=len(re.findall(r"\bOVER\s*\(",sql,re.I))
    sets=len(re.findall(r"\b(?:UNION(?:\s+ALL)?|INTERSECT|MINUS)\b",sql,re.I))
    groups=len(re.findall(r"\bGROUP\s+BY\b",sql,re.I))
    orders=len(re.findall(r"\bORDER\s+BY\b",sql,re.I))
    depth=_depth(sql)
    score=tables + joins*2 + subqueries*3 + ctes*2 + cases + aggregates + windows*2 + sets*2 + groups + orders + max(0,depth-1)
    band="low" if score<8 else "moderate" if score<18 else "high"
    return Metrics(tables,joins,subqueries,ctes,cases,aggregates,windows,sets,groups,orders,depth,score,band)
