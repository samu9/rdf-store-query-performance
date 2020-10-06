import time

import requests

from queries import QUERIES

ITERATIONS = 20

def measure_performance(db, query):      
    if db == "virtuoso":
        return sum([requests.get(query).elapsed.total_seconds() for x in range(ITERATIONS)]) / ITERATIONS
    if db == "graphdb":
        url="http://localhost:7200/repositories/KM4City"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        return sum([requests.request("POST", url, headers=headers, data = query).elapsed.total_seconds()  for x in range(ITERATIONS)]) / ITERATIONS

results = {
    "virtuoso": [],
    "graphdb": []
}
for i in range(len(QUERIES['virtuoso'])):
    results["virtuoso"].append(measure_performance("virtuoso", QUERIES['virtuoso'][i]))
    results["graphdb"].append(measure_performance("graphdb", QUERIES['graphdb'][i]))

print(results)