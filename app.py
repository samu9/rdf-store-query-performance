import time

import requests

from queries import QUERIES

def measure_performance(db, query):
    iterations = 20
    start = time.time()
    # print(requests.get(url).text)
    if db == "virtuoso":
        return sum([requests.get(query).elapsed.total_seconds() for x in range(iterations)]) / iterations
    if db == "graphdb":
        url="http://localhost:7200/repositories/KM4City"
        headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}
        return sum([requests.request("POST", url, headers=headers, data = query).elapsed.total_seconds()  for x in range(iterations)]) / iterations

results = {
    "virtuoso": [],
    "graphdb": []
}
for i in range(len(QUERIES['virtuoso'])):
    results["virtuoso"].append(measure_performance("virtuoso", QUERIES['virtuoso'][i]))
    results["graphdb"].append(measure_performance("graphdb", QUERIES['graphdb'][i]))

print(results)